from lab5.polynom.mon import Mon
from lab5.polynom.pol import Pol


def _f(f, args: tuple, table={}):
    if args in table:
        return table[args]
    elif len(args) == 1:
        x = args[0]
        y = table[args] = f(x)
        return y
    else:
        k = len(args) - 2
        y = table[args] = (_f(f, args[1:]) - _f(f, args[:-1]) ) / (args[-1] - args[0])
        return y


def interpolate(func, n: int, rg: tuple = (-1, 1), x: float = float('inf')) -> Pol:
    forward = True

    dx = (rg[1] - rg[0]) / (n - 1)

    # масив вузлів від початку проміжку до кінця включно з кроком dx
    nodes = [rg[0] + i * dx for i in range(n)]

    if x != float('inf'):
        forward = abs(nodes[0] - x) < abs(nodes[-1] - x)
        print(f'[{"вперед" if forward else "назад"}]')

    inter_polynom = Pol()

    if forward:

        for k in range(n):
            pol = Pol([Mon(1)])
            for i in range(k):
                pol *= Pol([Mon(1, 1), Mon(-nodes[i])])
            pol *= _f(func, tuple(nodes[:k+1]))
            inter_polynom += pol

    else:

        for k in range(n - 1, -1, -1):
            pol = Pol([Mon(1)])
            for i in range(n - 1, k, -1):
                pol *= Pol([Mon(1, 1), Mon(-nodes[i])])
            pol *= _f(func, tuple(nodes[k:]))
            inter_polynom += pol

    return inter_polynom
