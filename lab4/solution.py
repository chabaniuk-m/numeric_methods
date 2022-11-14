from testl import *
from test1 import *
from test2 import *


def relaxation_method(x_0: np.array, func, derivative, epsilon: float):
    tau = 1 / derivative(x_0).max()
    x = x_0 - func(x_0) * tau
    i = 0
    while np.max(np.abs(x - x_0)) >= epsilon:
        i += 1
        x_0 = x
        x = x_0 - func(x_0) * tau
    print(i)
    return x


def newton_method(x_0: np.array, func, derivative, epsilon: float) -> np.array:
    x = x_0
    i = 0
    while True:
        i += 1
        a = derivative(x)
        b = func(x)
        z = np.linalg.solve(a, b)
        x -= z
        if max(np.abs(z)) < epsilon:
            break
    print(i)
    return x


# actually this method cannot be applied in many cases
def modified_newton_method(x_0: np.array, func, derivative, epsilon: float) -> np.array:
    x = x_0
    a = np.linalg.inv(derivative(x))
    i = 0
    while True:
        i += 1
        b = func(x)
        z = np.linalg.solve(a, b)
        x -= z
        if max(np.abs(z)) < epsilon:
            break
    print(i)
    return x


if __name__ == "__main__":
    flag = 7
    if flag & 1:
        print("<<<Метод релаксації>>>\nтест із лекції:")
        sol = relaxation_method(np.array([0, 0]), test_l_func, test_l_derivative, 0.002)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_l_func(sol)}")
        print("тест 1:")
        sol = relaxation_method(np.array([2, 1.4]), test_1_func, test_1_derivative, 0.001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_1_func(sol)}")
        print("тест 2:")
        sol = relaxation_method(np.array([0, 1, 2, 3, 4]), test_2_func, test_2_derivative, 0.0001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_2_func(sol)}")
    if flag & 2:
        print("<<<Метод Ньютона>>>\nтест з лекції:")
        sol = newton_method([0, 0], test_l_func, test_l_derivative, 0.001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_l_func(sol)}")
        print("тест 1:")
        sol = newton_method([2, 1.4], test_1_func, test_1_derivative, 0.001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_1_func(sol)}")
        print("тест 2:")
        sol = newton_method([1, 1, 1, 1, 1], test_2_func, test_2_derivative, 0.1)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_2_func(sol)}")
    if flag & 4:
        print("<<<Модифікований метод Ньютона>>>\nтест з лекції: ")
        sol = modified_newton_method([0, 0], test_l_func, test_l_derivative, 0.2)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_l_func(sol)}")
        print("тест 1:")
        sol = modified_newton_method([2, 1.4], test_1_func, test_1_derivative, 0.001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_1_func(sol)}")
        print("тест 2:")
        sol = modified_newton_method([1, 1, 1, 1, 1], test_2_func, test_2_derivative, 0.001)
        print(f"наближений розв'язок - {sol}")
        print(f"нев'язка - {test_2_func(sol)}")
