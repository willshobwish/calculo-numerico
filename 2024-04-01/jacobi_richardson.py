import numpy as np


def jacobi_richardson(matrix_a, matrix_b, tolerance, x0, iterMax):
    lines_n, _ = np.shape(matrix_a)  # salva a quantidade de linhas em lines_n
    invert = np.linalg.inv(
        matrix_a * np.eye(lines_n)
    )  # salva a matriz inversa da diagonal principal da matriz matrix_a
    B = np.eye(lines_n) - invert @ matrix_a  # o @ é a multiplicação de matrizes
    d = invert @ matrix_b
    iterations = 0
    error = 1.0

    while error >= tolerance and iterations <= iterMax:
        x1 = (
            B @ x0 + d
        )  # o processo iterativo de jacobi_richardson é x(k+1) = Bx(k) + d
        error = np.max(abs(x1 - x0)) / np.max(abs(x1))
        x0 = x1
        iterations += 1

    return (x1, iterations)


matrix_a = [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
matrix_b = [[7], [-8], [6]]
lines_n, _ = np.shape(matrix_a)
x0 = np.zeros((lines_n, 1))
x1, iterations = jacobi_richardson(matrix_a, matrix_b, 0.0000000001, x0, 30)
print(f"Solução após {iterations} iterações é: ")
print(x1)
