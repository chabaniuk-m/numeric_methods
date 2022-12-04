from lab5.polynom.mon import Mon     # одночлен
from lab5.polynom.pol import Pol     # поліном


def interpolate(func, n: int, rg: tuple = (-1, 1)) -> Pol:
    """
    Формує інтерполяційний поліном Лагранжа
    на основі функції func
    :param func: функція, яка інтерполюється
    :param n: к-сть вузлів інтерполяції
    :param rg: закритий проміжок
    :return: інтерполяційний поліном лагранжа для функції func
    """
    if n < 2:
        raise ValueError("К-сть вузлів не може бути меншою за 2")
    elif not (len(rg) == 2 and isinstance(rg[0], (int, float)) and isinstance(rg[1], (int, float)) and rg[0] < rg[1]):
        raise ValueError("Проміжок повинен бути точкою, яка складається з 2-ох чисел, перше з яких є меншим")
    else:
        try:
            a = func((rg[0] + rg[1]) / 2)
            if not isinstance(a, (int, float)):
                raise TypeError
        except Exception:
            raise TypeError(f"Функція func повинна бути визначена не проміжку [{rg[0]}; {rg[1]}] (тобто приймати на вхід дійсне число й повертати як результат теж дійсне число")

    dx = (rg[1] - rg[0]) / (n - 1)

    # індекси | масив вузлів від початку проміжку до кінця включно з кроком dx | значення функції func для вузлів
    steps = range(n)
    nodes = [rg[0] + i * dx for i in range(n)]
    values = [func(node) for node in nodes]

    inter_polynom = Pol()

    for k in steps:
        numerator = Pol([Mon(1)])
        denominator = values[k]
        xk = nodes[k]
        for j in steps:
            if j != k:
                numerator *= Pol([Mon(1, 1), Mon(-nodes[j], 0)])
                denominator /= xk - nodes[j]
        inter_polynom += numerator * denominator

    return inter_polynom

