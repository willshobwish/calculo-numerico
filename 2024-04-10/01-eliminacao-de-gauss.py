import numpy as np


def gauss(matriz_a, vetor_b):
    matrix_new = matriz_a.copy()
    # print(f"Shape: {n}x{m}\nMatrix original:")
    for lines in matriz_a:
        print(lines)
    print("\nVetor independente original:")
    for lines in vetor_b:
        print(lines)
    print()
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
    print()
    print("Resultado vetor independente: ")
    # for lines in vetor_b:
    print(vetor_b)
    print()


def gauss_pivo(matriz_a, vetor_b):
    matrix_new = matriz_a.copy()
    # print(f"Shape: {n}x{m}\nMatrix original:")
    for lines in matriz_a:
        print(lines)
    print("\nVetor independente original:")
    for lines in vetor_b:
        print(lines)
    print()
    for k in range(0, len(matriz_a) - 1):
        for aux_index in range(k, len(matriz_a)):
            if abs(matriz_a[k][k]) < abs(matriz_a[aux_index][k]):
                aux = matriz_a[k].copy()
                matriz_a[k] = matriz_a[aux_index].copy()
                matriz_a[aux_index] = aux.copy()
                aux_vetor = vetor_b[k]
                vetor_b[k] = vetor_b[aux_index]
                vetor_b[aux_index] = aux_vetor
        for i in range(k + 1, len(matriz_a)):
            aik = matriz_a[i][k]
            for j in range(k, len(matriz_a)):
                matriz_a[i][j] = (
                    matriz_a[i][j] - matriz_a[k][j] * aik / matriz_a[k][k]
                )
            vetor_b[i] = vetor_b[i] - vetor_b[k] * aik / matriz_a[k][k]
    print("Resultado matriz:")
    for lines in matrix_new:
        print(lines)
    print()
    print("Resultado vetor independente: ")
    print(vetor_b)
    print("\n")


# gauss([[6, 2, -1], [2, 4, 1], [3, 2, 8]], vetor_b=[7, 7, 13])
# gauss_pivo([[3, 3, 1], [2, 2, -1], [1, -1, 5]], [7, 3, 5])

gauss_pivo([[3, 0, 3], [2, -2, 1], [1, 2, 0]], [1, 0, 0])
gauss_pivo([[3, 0, 3], [2, -2, 1], [1, 2, 0]], [0, 1, 0])
gauss_pivo([[3, 0, 3], [2, -2, 1], [1, 2, 0]], [0, 0, 1])

print(
    np.matmul(
        [[3, 0, 3], [2, -2, 1], [1, 2, 0]],
        [[1, -0.6666666666666666, -1], [0, 1, 1], [0, 0, 1]],
    )
)
