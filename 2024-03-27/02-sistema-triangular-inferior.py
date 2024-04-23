import numpy as np


def sistema_triangular_inferior(matrix_a, vetor_b):
    x = np.zeros((len(matrix_a), 1))
    x[0] = vetor_b[0] / matrix_a[0][0]

    for index in range(1, len(matrix_a)):
        somatorio = 0
        for index_j in range(0, len(matrix_a) - 1):
            somatorio += matrix_a[index_j][index] * x[index]
        x[index_j] = (vetor_b[index_j] - somatorio) / matrix_a[index_j][index_j]
    print()