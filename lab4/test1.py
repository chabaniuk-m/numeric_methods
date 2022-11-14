import numpy as np
from math import sin, cos


def test_1_func(x: np.array) -> np.array:
    """
    x^2/y^2 - cos(y) - 2 = 0
    x^2 + y^2 - 6  = 0
    """
    return np.array([x[0] ** 2 / x[1] ** 2 - cos(x[1]) - 2, x[0] ** 2 + x[1] ** 2 - 6])


def test_1_derivative(x: np.array) -> np.array:
    """
    2x/y^2   -2x^2/y^3 + sin(y)
    2x        2y
    """
    return np.array([
        [2 * x[0] / x[1] ** 2, -2 * x[0] ** 2 / x[1] ** 3 + sin(x[1])],
        [2 * x[0], 2 * x[1]]
    ])
