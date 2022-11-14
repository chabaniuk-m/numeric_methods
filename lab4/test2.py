import numpy as np


n = 5


def test_2_func(x: np.array) -> np.array:
    b = np.zeros(n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            b[i - 1] += j ** 3 if i == j else j ** 2
    result = np.zeros(n)
    for i in range(n):
        for j in range(n):
            result[i] += x[j] ** 3 if i == j else x[j] ** 2
        result[i] -= b[i]
    return result


def test_2_derivative(x: np.array) -> np.array:
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            result[i][j] += 3 * x[j] ** 2 if i == j else 2 * x[j]
    return result
