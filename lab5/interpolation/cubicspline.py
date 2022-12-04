from scipy.interpolate import CubicSpline


def interpolate(func, n: int, rg: tuple = (-1, 1)):
    dx = (rg[1] - rg[0]) / (n - 1)
    nodes = [rg[0] + i * dx for i in range(n)]

    return CubicSpline(nodes, [func(x) for x in nodes])