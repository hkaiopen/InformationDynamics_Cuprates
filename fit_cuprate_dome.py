import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# This script performs quantitative fitting of the superconducting dome of LSCO and YBCO 
# using the Information Dynamics relation T_c ∝ p_ID/(1-p_ID) with 
# p_ID^max=0.97 fixed from independent experiments.

# ========================== Experimental data ==========================
x_LSCO = np.array([0.00, 0.05, 0.07, 0.10, 0.12, 0.15, 0.18, 0.20, 0.25, 0.30])
Tc_LSCO = np.array([0, 12, 20, 28, 36, 40, 38, 32, 20, 8])

x_YBCO = np.array([0.00, 0.05, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.25])
Tc_YBCO = np.array([0, 40, 60, 75, 85, 93, 90, 80, 50])

p_max = 0.97          # fixed from strange metal and high-energy experiments

# ========================== Model definitions ==========================
def p_ID(x, A, x_opt):
    """Information purity: parabolic doping dependence, clipped to physical range."""
    p = p_max - A * (x - x_opt)**2
    return np.clip(p, 0.5, 0.99)

def Tc_model(x, s, A, x_opt):
    p = p_ID(x, A, x_opt)
    return s * p / (1 - p)

# ========================== Fit LSCO ==========================
popt_LSCO, _ = curve_fit(Tc_model, x_LSCO, Tc_LSCO, p0=[1.0, 5.0, 0.16])
s_LSCO, A_LSCO, x_opt_LSCO = popt_LSCO

# ========================== Fit YBCO ==========================
popt_YBCO, _ = curve_fit(Tc_model, x_YBCO, Tc_YBCO, p0=[2.5, 4.0, 0.14])
s_YBCO, A_YBCO, x_opt_YBCO = popt_YBCO

# ========================== Output parameters ==========================
print(f"LSCO : s = {s_LSCO:.2f}, A = {A_LSCO:.2f}, x_opt = {x_opt_LSCO:.3f}")
print(f"YBCO: s = {s_YBCO:.2f}, A = {A_YBCO:.2f}, x_opt = {x_opt_YBCO:.3f}")

# ========================== Smooth curves and plot ==========================
x_smooth = np.linspace(0, 0.30, 200)
Tc_LSCO_fit = Tc_model(x_smooth, s_LSCO, A_LSCO, x_opt_LSCO)
Tc_YBCO_fit = Tc_model(x_smooth, s_YBCO, A_YBCO, x_opt_YBCO)

plt.figure(figsize=(8, 5))
plt.scatter(x_LSCO, Tc_LSCO, label='LSCO exp', color='blue')
plt.plot(x_smooth, Tc_LSCO_fit, 'b-', label='ID fit (LSCO)')
plt.scatter(x_YBCO, Tc_YBCO, label='YBCO exp', color='red')
# Use raw string or avoid backslashes inside f-string:
plt.plot(x_smooth, Tc_YBCO_fit, 'r--', label=rf'ID fit (YBCO, $x_\mathrm{{opt}}$={x_opt_YBCO:.3f})')
plt.xlabel('Hole doping $x$')
plt.ylabel('$T_c$ (K)')
plt.title('Information dynamics: superconducting dome')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('dome_fit.pdf')
plt.show()