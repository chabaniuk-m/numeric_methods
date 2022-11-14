import math

import numpy as np
from fractions import Fraction


def read_web_graph() -> np.matrix:
    """
    Зчитує граф із файлу як матрицю суміжності,
    яка складається з 0 та 1
    :return: матрицю суміжності
    """
    with open('C:\\Users\\Admin\\PycharmProjects\\numeric_methods\\lab3\\graph.txt') as f:
        lst = f.readlines().copy()
        graph = []
        for line in lst:
            graph.append([int(x) for x in line.split(' ')])
        return np.matrix(graph)


def matrix_of_web_graph(web_graph: np.matrix) -> np.matrix:
    """
    Побудова матриці Маркова за веб графом
    :param web_graph: матриця, яка складається з 0 та 1,
    якщо між рядком i, та стовпцем j стоїть 1, тоді
    сторінка і посилається на сторінку j
    :return: матриця Маркова
    """
    # ціна посилання з кожної вершини
    link_cost = []
    n = len(web_graph)
    for i in range(n):
        denominator = 0
        for j in range(n):
            denominator += web_graph.item(i, j)
        link_cost.append(Fraction(1, denominator))
    a = []
    for j in range(n):
        row = []
        for i in range(n):
            # якщо сторінка і посилається на сторінку j, додамо до ціни сторінки j ціну посилання зі сторінки і
            row.append(Fraction(0) if web_graph.item(i, j) == 0 else link_cost[i])
        a.append(row)
    return np.matrix(a)


def get_B(n: int) -> np.matrix:
    a = []
    el = Fraction(1, n)
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(el)
        a.append(row)
    return np.matrix(a)


def build_M(A: np.matrix, B: np.matrix) -> np.matrix:
    return np.array(B) * Fraction(15, 100) + np.array(A) * Fraction(85, 100)


def get_x0(n: int) -> np.matrix:
    return np.matrix([Fraction(1, n) for _ in range(n)])


def norm(x: np.matrix):
    sum = 0
    for row in x:
        for el in row:
            sum += el ** 2
    return math.sqrt(sum)


def degree_method(A: np.matrix) -> np.matrix:
    xi = np.matrix(get_x0(len(A)).transpose())
    epsilon = 1e-4
    x = A * xi
    while norm(x - xi) >= epsilon:
        xi = x
        x = A * xi
    return x


A = matrix_of_web_graph(read_web_graph())
B = get_B(len(A))
M = build_M(A, B)
x = degree_method(M)

print("A = ")
print(A.astype(str))
print("B = ")
print(B.astype(str))
print("M = ")
print(M.astype(float))
print("x = ")
print(x.astype(float))
print("Mx = ")
print((M * x).astype(float))
