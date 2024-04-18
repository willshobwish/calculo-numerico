import numpy as np


def LUdecomposition(matrix_a: list):
    m, n = np.shape(matrix_a)
    matrix_zero = np.zeros(shape=(m, n))
    identity_matrix = np.eye(N=n, M=m)

    for index_i, element_i in enumerate(matrix_a):
        for index_j, element_j in enumerate(matrix_a[index_i]):
            if index_i <= index_j:
                if index_i == 1:
                    matrix_zero[index_i][index_j] = matrix_a[index_i][index_j]
                else:
                    somatorio = 0
                    for index_k in range(0, index_i):
                        somatorio += np.dot(
                            identity_matrix[index_i][index_k],
                            matrix_zero[index_k][index_j],
                        )
                    matrix_zero[index_i][index_j] = (
                        matrix_a[index_i][index_j] - somatorio
                    )
            else:
                if index_j == 1:
                    identity_matrix[index_i][index_j] = (
                        matrix_a[index_i][index_j] / matrix_zero[index_j][index_j]
                    )
                else:
                    somatorio = 0
                    for index_k in range(0, index_j):
                        somatorio += np.dot(
                            identity_matrix[index_i][index_k],
                            matrix_zero[index_k][index_j],
                        )
                    identity_matrix[index_i][index_j] = (
                        matrix_a[index_i][index_j] - somatorio
                    ) / matrix_zero[index_j][index_j]
    print(f"Matriz nula:\n{matrix_zero}\n")
    print(f"Matriz identidade:\n{identity_matrix}\n")
    print(f"Matriz A:\n{matrix_a}\n")


LUdecomposition([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
