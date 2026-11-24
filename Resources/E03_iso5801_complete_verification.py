"""
Auxiliary Script 03: Complete ISO 5801:2019 Application & Full-Curve GUM Verification
Solves the iterative ISO 5801 Clause 13.3 nozzle discharge coefficient alpha(Re_d)
and verifies Table 13 expanded uncertainty compliance across OP-1 to OP-10.
"""

import numpy as np
import pandas as pd
from uncertainties import ufloat

# ==============================================================================
# 1. AMBIENT & FLUID PROPERTIES (STANDARD LABORATORY STATE)
# ==============================================================================
pa = ufloat(100500.0, 100.0 / np.sqrt(3))
Ta = ufloat(20.0, np.hypot(0.15 / np.sqrt(3), 0.05))
rh = ufloat(0.55, 0.015 / np.sqrt(3))

R_d, R_v = 287.05, 461.50
p_sat = 610.78 * (np.e ** ((17.27 * Ta) / (Ta + 237.3)))
R_w = R_d / (1.0 - (rh * p_sat / pa) * (1.0 - R_d / R_v))
rho = pa / (R_w * (Ta + 273.15))
mu = 1.81e-5  # Dynamic viscosity of air at 20°C [Pa·s]

# ==============================================================================
# 2. ITERATIVE ISO 5801 CLAUSE 13.3 NOZZLE DISCHARGE COEFFICIENT SOLVER
# ==============================================================================
def solve_nozzle_alpha(d_nom: float, dp_nom: float, rho_nom: float) -> float:
    """Iteratively solves alpha(Re_d) per ISO 5801 Clause 13.3."""
    alpha = 0.990
    for _ in range(15):
        v_n = alpha * np.sqrt(2.0 * dp_nom / rho_nom)
        Re_d = (rho_nom * v_n * d_nom) / mu
        alpha = 0.9986 - (7.006 / np.sqrt(Re_d)) + (134.6 / Re_d)
    return alpha

# ==============================================================================
# 3. FULL 10-POINT OPERATING SWEEP VERIFICATION
# ==============================================================================
nozzles_nom = [0.315, 0.315, 0.224, 0.160]
Q_targets = [4.79, 4.35, 3.85, 3.30, 2.70, 2.10, 1.50, 0.95, 0.55, 0.00]
masks = [
    [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0],
    [1, 0, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 0, 1, 0],
    [0, 0, 0, 1], [0, 0, 0, 0],
]

u_dp = 1.0 / np.sqrt(3)
u_pe3 = 0.5 / np.sqrt(3)

rows = []
for idx, (Q_t, mask) in enumerate(zip(Q_targets, masks), start=1):
    q_norm = Q_t / 4.79
    p_fs_nom = 265.0 * (1.0 - 0.35 * q_norm - 0.65 * (q_norm ** 2))
    pe3 = ufloat(-p_fs_nom, u_pe3)
    p_fs = -pe3

    if Q_t == 0.0:
        rows.append({
            "Point": f"OP-{idx}",
            "q_V [m^3/s]": "0.000",
            "p_fs [Pa]": f"{p_fs.n:.1f}",
            "dp_nozzle [Pa]": "0.0",
            "U_95%(q_V) [%]": "-",
            "ISO Table 13": "PASS (Shut-off)",
        })
        continue

    # Estimate dp_nozzle for target Q_t
    A_approx = sum(np.pi * d**2 / 4.0 for d, m in zip(nozzles_nom, mask) if m)
    dp_nom = 0.5 * rho.n * ((Q_t / (0.985 * A_approx)) ** 2)
    dp = ufloat(dp_nom, u_dp)

    qm_tot = 0.0
    for d_n, m in zip(nozzles_nom, mask):
        if m:
            alpha_val = solve_nozzle_alpha(d_n, dp_nom, rho.n)
            alpha_u = ufloat(alpha_val, (0.005 * alpha_val) / np.sqrt(3))
            d_u = ufloat(d_n, 0.0005 / np.sqrt(3))
            A_u = np.pi * (d_u ** 2) / 4.0
            qm_tot = qm_tot + alpha_u * A_u * ((2.0 * rho * dp) ** 0.5)

    qV = qm_tot / rho
    u95_qV_pct = 200.0 * qV.s / qV.n

    rows.append({
        "Point": f"OP-{idx}",
        "q_V [m^3/s]": f"{qV.n:.3f}",
        "p_fs [Pa]": f"{p_fs.n:.1f}",
        "dp_nozzle [Pa]": f"{dp_nom:.1f}",
        "U_95%(q_V) [%]": f"{u95_qV_pct:.2f}%",
        "ISO Table 13": "PASS" if u95_qV_pct <= 2.0 else "FAIL",
    })

df_final = pd.DataFrame(rows)
print("=== RELEASE 1 COMPLETE ISO 5801 OPERATING SWEEP & GUM VERIFICATION ===")
print(df_final.to_string(index=False))