"""
Auxiliary Script 01: Nominal Dimensionless Parameters of S&P HCFB/4-630/H
Verifies tip speed, machine Reynolds number Re_D, and dimensionless coefficients.
"""
import numpy as np

D1 = 0.630          # Impeller diameter [m]
A1 = np.pi * D1**2 / 4.0
N0 = 1380.0         # Nominal speed [rpm]
n0 = N0 / 60.0      # Rotational frequency [rev/s]
u_tip = np.pi * n0 * D1

rho0 = 1.20         # Reference air density [kg/m^3]
mu = 1.81e-5        # Dynamic viscosity at 20°C [Pa·s]

# 1. Free delivery point (qV = 4.79 m^3/s, p_fs = 0 Pa, Pa ~ 1150 W)
qV_fd = 4.79
v1_fd = qV_fd / A1
pd1_fd = 0.5 * rho0 * v1_fd**2
Pa_fd = 1150.0

phi_fd = qV_fd / (A1 * u_tip)
psi_t_fd = pd1_fd / (0.5 * rho0 * u_tip**2)
lam_fd = Pa_fd / (0.5 * rho0 * A1 * u_tip**3)
eta_t_fd = (qV_fd * pd1_fd) / Pa_fd
Re_D = (rho0 * u_tip * D1) / mu

print(f"Tip Speed u_tip         : {u_tip:.2f} m/s")
print(f"Machine Reynolds Re_D   : {Re_D:.2e} (Self-similar turbulent regime)")
print(f"Free Delivery phi       : {phi_fd:.3f}")
print(f"Free Delivery psi_t     : {psi_t_fd:.3f}")
print(f"Free Delivery lambda    : {lam_fd:.3f}")
print(f"Free Delivery eta_total : {eta_t_fd*100:.1f} %")