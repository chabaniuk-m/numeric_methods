import math
from lab5.interpolation import lagrange
from lab5.interpolation import newton
from lab5.interpolation import cubicspline
from matplotlib import pyplot as plt


# f = lambda x: -3*x**4 + 18*x**3 + -23*x**2 + 109*x - 59
# f = lambda x: math.sin(x) * math.cos(x) * 10
f = lambda x: math.log2(0.2*x) * math.sin(4*x)
n = 9
rg = (1, 10)
x = 9
dx = (rg[1] - rg[0]) / (100*n - 1)
nodes = [rg[0] + i * dx for i in range(100*n)]

plt.plot(nodes, [f(x) for x in nodes], color='black', linestyle=':')

inter_polynom = lagrange.interpolate(f, n, rg)

plt.plot(nodes, [inter_polynom(x) for x in nodes], color="#6ce036")
print("Інтерполяційний поліном Лагранжа L(x):")
print(inter_polynom)
print(f"L({x}) = {inter_polynom(x)}")

print("-------------------------------------------------")

inter_polynom = newton.interpolate(f, n, rg, x)

plt.plot(nodes, [inter_polynom(x) for x in nodes], color="#e06e36")
print("Інтерполяційний поліном Ньютона N(x):")
print(inter_polynom)
print(f"N({x}) = {inter_polynom(x)}")

print("-------------------------------------------------")

cs = cubicspline.interpolate(f, n, rg)

plt.plot(nodes, cs(nodes), color="#aa36e0")
# plt.plot(nodes, cs(nodes, 1), color="#ddd")
# plt.plot(nodes, cs(nodes, 2), color="#ddd")
# plt.plot(nodes, cs(nodes, 3), color="#ddd")
# plt.plot(nodes, cs(nodes, 4), color="#ddd")

dx = (rg[1] - rg[0]) / (n - 1)
nodes = [rg[0] + i * dx for i in range(n)]

plt.plot(nodes, [f(x) for x in nodes], color='darkorange', linewidth=0, marker='s')

plt.legend(["f(x)", "Lagrange", "Newton", "Cubic Spline"], loc='upper center')
plt.show()
