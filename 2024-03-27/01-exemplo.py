import numpy as np


def Sistema_triangular_superior(matriz_a: list, vetor_b: list):
    n = len(matriz_a)
    x = np.zeros(n)
    x[n] = vetor_b[n] / matriz_a[n][n]
    for k in range(1, n):
        somatorio = 0
        for i in range((n - k) + 1, n):
            somatorio += matriz_a[n - k][i] * x[i]
        x[n - k] = (vetor_b[n - k] - somatorio) / matriz_a[n - k][n - k]
    return x


print(Sistema_triangular_superior([[2, 1, 3], [0, 1, -1], [0, 0, 2]], [11, 1, 4]))
