import numpy as np


def sistema_triangular_superior(A, b):
    n = len(A)
    x = np.zeros((n, n))
    x[n] = b[n] / A[n][n]

    for k in range(0, n):
        somatorio = 0
        for i in range((n - k + 1), n):
            somatorio += A[n - k][i] * x[i]
        x[n - k] = b[n - k] - somatorio / A[n - k][n - k]
    return x
