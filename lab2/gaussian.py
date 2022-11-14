from fractions import Fraction
import numpy as np


def gaussian_method(A: np.ndarray, b: np.ndarray) -> np.array:
    n = len(b)
    x = np.empty(n, dtype=Fraction)
    for i in range(n):
        swap(A, b, i, row_index_of_max_element(A, i))
        reduce_following_rows(A, b, i)
    for k in range(n, 0, -1):
        i = k - 1
        x[i] = b[i]
        for s in range(k, n):
            x[i] -= A[i][s] * x[s]
    return x


def swap(A, b, i, j):
    A[i], A[j] = A[j].copy(), A[i].copy()
    b[i], b[j] = b[j], b[i]


def row_index_of_max_element(A, j):
    idx, val = j, abs(A[j][j])
    for i in range(j + 1, len(A)):
        if abs(A[i][j]) > val:
            val = abs(A[i][j])
            idx = i
    return idx


def reduce_following_rows(A, b, i):
    # avoid division by zero
    if A[i][i] == 0:
        j = 0
        for k in range(i + 1, len(A)):
            if A[k][i] != 0:
                j = k
                break
        swap(A, b, i, j)

    a_ii = A[i][i]
    n = len(A)
    for j in range(i, n):
        A[i][j] /= a_ii
    b[i] /= a_ii
    for k in range(i + 1, n):
        m = A[k][i]
        for j in range(i, n):
            A[k][j] -= m * A[i][j]
        b[k] -= m * b[i]


def generate_gilbert(n: int) -> np.ndarray:
    A = np.empty([n, n], dtype=Fraction)
    for i in range(n):
        for j in range(n):
            A[i][j] = Fraction(1, i + j + 1)
    return A


def test(filepath: str):
    file = open(filepath)
    lines = file.readlines()
    n = int(lines[0])

    # init matrix A
    A = np.empty([n, n], dtype=Fraction)
    for i in range(1, n + 1):
        line = lines[i].split("\t")
        for j in range(n):
            A[i - 1][j] = Fraction(int(line[j]))

    # init vector b
    b = np.empty(n, dtype=Fraction)
    line = lines[n + 1].split("\t")
    for k in range(n):
        b[k] = Fraction(int(line[k]))

    x_actual = gaussian_method(A, b)

    # init result vector x
    x = np.empty(n, dtype=int)
    line = lines[n + 2].split("\t")
    for k in range(n):
        x[k] = int(line[k])

    print(gaussian_method(A, b), "\n")
    n = int(input("Введіть розмірність матриці Гільберта: "))
    A = generate_gilbert(n)
    b = np.empty(n, dtype=Fraction)
    for i in range(n):
        sum = Fraction(0)
        for j in A[i]:
            sum += j
        b[i] = sum
    print(gaussian_method(A, b))


# file with system with linear equation and exact solution
test("C:\\Users\\Admin\\Desktop\\education\\ЧМ\\лаб2\\test_gauss_1.txt")






