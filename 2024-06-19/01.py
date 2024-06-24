import math
import numpy as np
def produto(x1:list,x2:list):
    # print(x1)
    # print(x2)
    if len(x1) == len(x2):
       soma=0
       for index, i in enumerate(x1):
            soma+=x1[index]*x2[index]
    else:
        print("Vetores não iguais")
    return soma

def polinomio(u1,u2):
    u0 = np.ones(len(u1))
    un = [u0,u1,u2]
    matrix= np.zeros((3,3))
    for index, item in enumerate(un):
        for index_j, item_j in enumerate(un):
            matrix[index,index_j]=produto(un[index],un[index_j])
    print(matrix)
    return matrix

def gauss(matriz_a, vetor_b):
    matrix_new = matriz_a.copy()
    # print(f"Shape: {n}x{m}\nMatrix original:")
    # for lines in matriz_a:
    #     print(lines)
    # print("\nVetor independente original:")
    # for lines in vetor_b:
    #     print(lines)
    # print()
    for k in range(0, len(matriz_a) - 1):
        for i in range(k + 1, len(matriz_a)):
            aik = matriz_a[i][k]
            for j in range(k, len(matriz_a)):
                matrix_new[i][j] = (
                    matriz_a[i][j] - matriz_a[k][j] * aik / matriz_a[k][k]
                )
            vetor_b[i] = vetor_b[i] - vetor_b[k] * aik / matriz_a[k][k]
    print("Resultado matriz:")
    # for lines in matrix_new:
    print(matrix_new)
    # print()
    print("Resultado vetor independente: ")
    # for lines in vetor_b:
    print(vetor_b)
    print()

def gauss_fix(matriz_a, vetor_b):
    n = len(matriz_a)
    # Creating deep copies of matriz_a and vetor_b
    matrix_new = [row[:] for row in matriz_a]
    vector_new = vetor_b[:]

    for k in range(n - 1):
        if matrix_new[k][k] == 0:
            raise ValueError("Zero pivot element detected, cannot proceed with Gaussian elimination.")
        for i in range(k + 1, n):
            factor = matrix_new[i][k] / matrix_new[k][k]
            for j in range(k, n):
                matrix_new[i][j] -= factor * matrix_new[k][j]
            vector_new[i] -= factor * vector_new[k]
    return vector_new

def gauss_elimination(matriz_a, vetor_b):
    n = len(matriz_a)
    # Creating deep copies of matriz_a and vetor_b
    matrix_new = [row[:] for row in matriz_a]
    vector_new = vetor_b[:]

    for k in range(n - 1):
        if matrix_new[k][k] == 0:
            raise ValueError("Zero pivot element detected, cannot proceed with Gaussian elimination.")
        for i in range(k + 1, n):
            factor = matrix_new[i][k] / matrix_new[k][k]
            for j in range(k, n):
                matrix_new[i][j] -= factor * matrix_new[k][j]
            vector_new[i] -= factor * vector_new[k]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = sum(matrix_new[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (vector_new[i] - sum_ax) / matrix_new[i][i]

    return x

print(gauss(polinomio([0,1,2,3],[0,1,4,9]),[2.5,11.4,17.8]))