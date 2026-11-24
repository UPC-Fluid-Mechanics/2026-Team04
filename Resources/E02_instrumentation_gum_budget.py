"""
Auxiliary Script 02: Instrumentation Uncertainty Budget (GUM / ISO 5801 Table 13)
Combines transducer accuracy + NI cDAQ module error (Type B, k=1 and k=2)
and checks compliance at the nominal Best Efficiency Point (BEP).
"""

import numpy as np
import pandas as pd
from uncertainties import ufloat

def type_b_rect(half_width: float) -> float:
    """Converts a rectangular ±a tolerance bound into a 1-sigma standard uncertainty."""
    return half_width / np.sqrt(3.0)

# ==============================================================================
# 1. INSTRUMENT + DAQ COMBINED TYPE B UNCERTAINTIES (k = 1)
# ==============================================================================
# NI-9205 (0-10 V range) absolute accuracy at full scale ~ 1.5 mV (0.015% FS)
daq_v_rel = 0.00015

u_dp = np.hypot(type_b_rect(1.0), type_b_rect(daq_v_rel * 1000.0))       # [Pa] (0..1000 Pa)
u_pe3 = np.hypot(type_b_rect(0.5), type_b_rect(daq_v_rel * 1000.0))      # [Pa] (-500..+500 Pa)
u_pa = np.hypot(type_b_rect(100.0), type_b_rect(daq_v_rel * 30000.0))    # [Pa] (800..1100 hPa span = 30000 Pa)
u_T = np.hypot(type_b_rect(0.15), type_b_rect(0.05))                     # [°C] Pt100 Cl.A + NI-9217
u_rh = np.hypot(type_b_rect(0.015), type_b_rect(daq_v_rel * 1.0))        # [-]  0..100% RH
u_M = np.hypot(type_b_rect(0.04), type_b_rect(daq_v_rel * 20.0))         # [N·m] 0..20 N·m
u_N = type_b_rect(1.0)                                                   # [rpm] NI-9401 encoder

# ==============================================================================
# 2. NOMINAL BEP EVALUATION (qV ~ 3.30 m^3/s, p_fs ~ 145 Pa, N = 1380 rpm)
# ==============================================================================
pa = ufloat(100500.0, u_pa)
Ta = ufloat(20.0, u_T)
rh = ufloat(0.55, u_rh)

# Humid air density (ISO 5801 Eqs. 25 & 26)
R_d, R_v = 287.05, 461.50
p_sat = 610.78 * (np.e ** ((17.27 * Ta) / (Ta + 237.3)))
R_w = R_d / (1.0 - (rh * p_sat / pa) * (1.0 - R_d / R_v))
rho = pa / (R_w * (Ta + 273.15))

# Active nozzles at BEP: 315 + 315 + 224 mm (A_open = 0.1952 m^2 -> dp ~ 175 Pa)
d_list = [ufloat(0.315, type_b_rect(0.0005)),
          ufloat(0.315, type_b_rect(0.0005)),
          ufloat(0.224, type_b_rect(0.0005))]
alpha = ufloat(0.985, type_b_rect(0.005 * 0.985))
dp = ufloat(175.0, u_dp)

qm = sum(alpha * (np.pi * d**2 / 4.0) * (2.0 * rho * dp)**0.5 for d in d_list)
qV = qm / rho

# Fan pressures & shaft power at BEP
D1 = 0.630
A1 = np.pi * D1**2 / 4.0
pe3 = ufloat(-145.0, u_pe3)
p_fs = -pe3
p_d1 = 0.5 * rho * (qV / A1)**2
p_f = p_fs + p_d1

M = ufloat(8.65, u_M)
N = ufloat(1380.0, u_N)
Pa = M * (2.0 * np.pi * N / 60.0)
eta_t = (qV * p_f) / Pa

# Summary Table vs ISO 5801 Table 13 Limits
summary = pd.DataFrame([
    {"Variable": "Air Density (rho)", "Nominal": f"{rho.n:.4f} kg/m^3", "U_95% [%]": 200 * rho.s / rho.n, "ISO 5801 Table 13 Limit [%]": 0.5},
    {"Variable": "Volumetric Flow (q_V)", "Nominal": f"{qV.n:.3f} m^3/s", "U_95% [%]": 200 * qV.s / qV.n, "ISO 5801 Table 13 Limit [%]": 2.0},
    {"Variable": "Fan Total Pressure (p_f)", "Nominal": f"{p_f.n:.1f} Pa", "U_95% [%]": 200 * p_f.s / p_f.n, "ISO 5801 Table 13 Limit [%]": 1.4},
    {"Variable": "Impeller Shaft Power (P_a)", "Nominal": f"{Pa.n:.1f} W", "U_95% [%]": 200 * Pa.s / Pa.n, "ISO 5801 Table 13 Limit [%]": 2.0},
    {"Variable": "Fan Total Efficiency (eta_t)", "Nominal": f"{eta_t.n*100:.1f} %", "U_95% [%]": 200 * eta_t.s / eta_t.n, "ISO 5801 Table 13 Limit [%]": 2.8},
])
summary["Compliance"] = np.where(summary["U_95% [%]"] <= summary["ISO 5801 Table 13 Limit [%]"], "PASS", "FAIL")

print("=== GUM INSTRUMENTATION BUDGET AT BEP (k = 2, 95% CONFIDENCE) ===")
print(summary.to_string(index=False, float_format=lambda x: f"{x:.2f}"))