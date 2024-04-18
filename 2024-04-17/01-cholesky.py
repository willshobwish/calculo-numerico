import numpy as np
import math

# np.transpose()


def binet(matrix):
    matrix = np.array(matrix)
    determinante = 1
    for i, _ in enumerate(matrix):
        determinante = determinante * matrix[i][i] ** 2
    return determinante


def cholesky(matrix):
    matrix = np.array(matrix)
    matrix_g = np.tril(matrix)
    matrix_t = np.transpose(matrix_g)
    print(
        f"Matriz:\n{matrix}\n\nMatriz triangular inferior:\n{matrix_g}\n\nMatriz transposta:\n{matrix_t}\n"
    )
    for i, _ in enumerate(matrix_g):
        for j, _ in enumerate(matrix_t):
            if i == 0 and j == 0:
                matrix_g[i][j] = math.sqrt(matrix[i][j])
            elif j == 0:
                matrix_g[i][j] = matrix_g[i][0] / matrix_g[0][0]
            elif i == j:
                somatorio = 0
                for k in range(0, i):
                    somatorio += matrix_g[i][k] ** 2
                matrix_g[i][j] = math.sqrt(matrix[i][j] - somatorio)
            else:
                somatorio = 0
                for k in range(0, j):
                    somatorio += matrix_g[i][k] * matrix_g[j][k]
                matrix_g[i][j] = (matrix[i][j] - somatorio) / matrix_g[j][j]
    print(f"Matriz resultado:\n{matrix_g}\n")
    print(f"Prova:\n{np.matmul(matrix_g, matrix_t)}")
    return matrix_g


print(binet(cholesky([[4, 2, -4], [2, 10, 4], [-4, 4, 9]])))
