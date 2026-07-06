import numpy as np
from scipy import integrate

def f(x):
    return np.exp(x**2)

a, b = 0, 1

exact, _ = integrate.quad(f, a, b)

# بخش الف
n = 100
x = np.linspace(a, b, n)
y = f(x)

trap = np.trapezoid(y, x)
simp = integrate.simpson(y, x=x)

# بخش ب
gauss, _ = integrate.fixed_quad(f, a, b, n=3)

print("="*60)
print(f"{'روش':<20} {'مقدار':<20} {'خطای مطلق':<15}")
print("="*60)
print(f"{'مرجع (quad)':<20} {exact:<20.10f} {'-':<15}")
print(f"{'ذوزنقه‌ای':<20} {trap:<20.10f} {abs(trap-exact):<15.2e}")
print(f"{'سیمپسون':<20} {simp:<20.10f} {abs(simp-exact):<15.2e}")
print(f"{'گوسی (n=3)':<20} {gauss:<20.10f} {abs(gauss-exact):<15.2e}")
print("="*60)

print("\nهمگرایی انتگرال گوسی:")
print("-"*50)
for n_gauss in [1, 2, 3, 5, 10]:
    g, _ = integrate.fixed_quad(f, a, b, n=n_gauss)
    print(f"n={n_gauss:<2d} | مقدار: {g:.10f} | خطا: {abs(g-exact):.2e}")
