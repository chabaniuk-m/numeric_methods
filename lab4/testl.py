import numpy as np
from math import sin, cos


def test_l_func(x: np.array) -> np.array:
    """
    x - 1/2 * sin((x - y)/2) = 0
    y - 1/2 * cos((x + y)/2) = 0
    """
    return np.array([x[0] - 0.5 * sin((x[0] - x[1]) / 2), x[1] - 0.5 * cos((x[0] + x[1]) / 2)])


def test_l_derivative(x: np.array) -> np.array:
    """
    1 - 0.25cos((x - y) / 2)    0.25cos((x - y) / 2)
      0.25sin((x + y) / 2)     1 + 0.25sin((x + y) / 2)
    """
    return np.array([
        [1 - 0.25 * cos((x[0] - x[1]) / 2), 0.25 * cos((x[0] - x[1]) / 2)],
        [0.25 * sin((x[0] + x[1]) / 2), 1 + 0.25 * sin((x[0] + x[1]) / 2)]
    ])
