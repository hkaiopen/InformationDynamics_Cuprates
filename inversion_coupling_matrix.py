"""
Inversion of the coupling matrix K(x) from superfluid density data.
Assumes: K(r) = K0 + dK(x) * cos(qx)cos(qy) with q = pi.
Linear response: n_s_exp = n_s_uniform + chi * (dK)^2
We solve for dK(x) given n_s_exp(x) and the uniform GL prediction.

Author: Kai Huang
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ========================================
# 1. Generate synthetic "experimental" data
# ========================================
# Doping range
x_vals = np.linspace(0.05, 0.30, 20)
x_opt = 0.16
p_max = 0.97
A = 5.0
s0 = 30.0  # K

def purity(x):
    return p_max - A * (x - x_opt)**2

def Tc_phenom(x):
    p = purity(x)
    return s0 * p / (1 - p)

# Uniform GL prediction: n_s_uniform = epsilon/gamma, with epsilon ~ T_c
gamma = 1.0
const = 1.0
n_s_uniform = Tc_phenom(x_vals) / const   # arbitrary scaling

# Assume true dK(x) has a peak near quantum critical point x_QCP = 0.19
x_QCP = 0.19
w = 0.03
dK_max_true = 0.6
dK_true = dK_max_true * np.exp(-((x_vals - x_QCP)/w)**2)

# Linear response coefficient chi (obtained from separate simulation or theory)
chi = 0.8   # typical value, positive means enhanced n_s

# Experimental n_s: uniform + chi*dK^2 + noise
noise_std = 0.02
n_s_exp = n_s_uniform + chi * dK_true**2
n_s_exp += np.random.normal(0, noise_std, size=len(x_vals))

# Ensure positivity
n_s_exp = np.maximum(n_s_exp, 0.01)

print("=" * 60)
print("Synthetic experimental data generated")
print(f"x range: {x_vals[0]:.3f} - {x_vals[-1]:.3f}")
print(f"True dK peak at x={x_QCP:.3f}, amplitude={dK_max_true:.3f}")
print(f"Added Gaussian noise std={noise_std:.3f}")
print("=" * 60)

# ========================================
# 2. Inversion: solve for dK(x) from n_s_exp
# ========================================
# We assume n_s_uniform is known from the dome fit (T_c fit).
# Then dK_sq = (n_s_exp - n_s_uniform) / chi
dK_sq_inv = (n_s_exp - n_s_uniform) / chi
# Negative values can arise from noise; set to zero (no coupling)
dK_sq_inv = np.maximum(dK_sq_inv, 0.0)
dK_inv = np.sqrt(dK_sq_inv)

# Fit a Gaussian shape to the inverted dK to extract peak position and width
def gaussian(x, amp, center, sigma):
    return amp * np.exp(-((x - center)/sigma)**2)

try:
    popt, pcov = curve_fit(gaussian, x_vals, dK_inv, p0=[0.5, 0.19, 0.03])
    dK_fit = gaussian(x_vals, *popt)
    print("\nFitted Gaussian parameters for dK(x):")
    print(f"  Amplitude = {popt[0]:.4f}")
    print(f"  Center = {popt[1]:.4f}")
    print(f"  Width = {popt[2]:.4f}")
except Exception as e:
    print("Gaussian fit failed:", e)
    dK_fit = dK_inv

# ========================================
# 3. Plot results
# ========================================
plt.figure(figsize=(10, 8))

plt.subplot(2,2,1)
plt.plot(x_vals, n_s_uniform, 'b-', label='Uniform GL (no K)')
plt.plot(x_vals, n_s_exp, 'ro', markersize=3, label='Synthetic data (with K)')
plt.xlabel('Hole doping x')
plt.ylabel('Superfluid density n_s (arb. units)')
plt.title('Input: n_s data (uniform + K effect)')
plt.legend()
plt.grid(True, linestyle=':')

plt.subplot(2,2,2)
plt.plot(x_vals, dK_true, 'g-', label='True dK(x)')
plt.plot(x_vals, dK_inv, 'ro', markersize=3, label='Inverted dK (from n_s)')
plt.plot(x_vals, dK_fit, 'b--', label='Gaussian fit')
plt.xlabel('Hole doping x')
plt.ylabel('dK(x) (coupling amplitude)')
plt.title('Inversion: dK(x) from superfluid density')
plt.legend()
plt.grid(True, linestyle=':')

plt.subplot(2,2,3)
residual = dK_inv - dK_true
plt.plot(x_vals, residual, 'ko', markersize=3)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Hole doping x')
plt.ylabel('Residual (inverted - true)')
plt.title('Inversion error (noise dependent)')
plt.grid(True, linestyle=':')

plt.subplot(2,2,4)
plt.plot(x_vals, n_s_exp - n_s_uniform, 'ro', label='Excess n_s')
plt.plot(x_vals, chi * dK_true**2, 'b-', label='Chi * dK^2 (true)')
plt.xlabel('Hole doping x')
plt.ylabel('Excess superfluid density')
plt.title('Linear response: excess n_s ∝ dK^2')
plt.legend()
plt.grid(True, linestyle=':')

plt.tight_layout()
plt.savefig('inversion_coupling_matrix.png', dpi=150)
plt.show()

print("\nFigure saved as inversion_coupling_matrix.png")
print("Done.")