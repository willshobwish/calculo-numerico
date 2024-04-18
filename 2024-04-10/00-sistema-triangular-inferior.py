import numpy as np


def sistema_triangular_inferior(matrix, b):
    matrix = np.array(matrix)
    x = np.zeros((len(matrix)))
    x[0] = b[0] / matrix[0][0]
    for k in range(1, len(matrix)):
        somatorio = 0
        for i in range(0, k):
            somatorio += matrix[k][i] * x[i]

        x[k] = (b[k] - somatorio) / matrix[k][k]
    print(f"Matriz:\n{matrix}\n\nVetor:\n{x}\n")


sistema_triangular_inferior([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3])
