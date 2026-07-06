import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial

x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([1, 3, 5, 8, 5, 2], dtype=float)

poly_lagrange = lagrange(x, y)
lagrange_formula = Polynomial(poly_lagrange.coef[::-1])

cs = CubicSpline(x, y, bc_type='natural')

x_new = np.linspace(1, 6, 100)
y_lagrange = poly_lagrange(x_new)
y_spline = cs(x_new)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', zorder=5, label='Main Points')
plt.plot(x_new, y_lagrange, label='Lagrange Interpolation', linestyle='--')
plt.plot(x_new, y_spline, label='Cubic Spline', linestyle='-')
plt.legend()
plt.title('Comparison: Lagrange vs Cubic Spline')
plt.grid(True)
plt.show()

print("-" * 30)
print("1. Lagrange Polynomial Formula:")
print(lagrange_formula)
print("\n" + "-" * 30)
print("2. Cubic Spline Coefficients (for each interval):")

for i in range(len(x) - 1):
    print(f"Interval [{x[i]}, {x[i+1]}]:")
    print(f"  S_{i}(x) = {cs.c[0,i]:.6f}(x-{x[i]})^3 + {cs.c[1,i]:.6f}(x-{x[i]})^2 + {cs.c[2,i]:.6f}(x-{x[i]}) + {cs.c[3,i]:.6f}")
