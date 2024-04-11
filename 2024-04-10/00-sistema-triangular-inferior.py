import numpy as np


def sistema_triangular_inferior(matrix_A):
    n, m = np.shape(matrix_A)
    zero_matrix = np.zeros((n, 1))
    zero_matrix[1] = 