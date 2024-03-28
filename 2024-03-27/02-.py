import numpy as np


def decomposition(matrix_a):
    n = len(matrix_a)
    l = np.identity(n)
    u = np.identity(n)
    for p in range(0, n):
        for j in range(p, n):
            soma = 0
            if p != 1:
                for k in range(0, p):
                    soma += l[p][k] * u[k][j]
            u[p][j] = matrix_a[p][j] - soma

        if p != n:
            for i in range(p + 2, n):
                soma = 0
                for k in range(1, p):
                    soma += l[i][k] * u[k][p]
                l[i][p] = (matrix_a[i][p] - soma) / u[p][p]
        l[p][p] = 1
    print(l)
    print(u)


decomposition([[5, 2, 1], [3, 1, 4], [1, 1, 3]])
