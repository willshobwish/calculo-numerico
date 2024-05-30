import math
import numpy as np


def trapezios_generalizada(x: list, y: list):
    soma = 0
    y_soma = y[1 : len(x)]
    # print(y_soma)
    for i in y_soma:
        soma += i
    soma = y[0] + 2 * soma + y[-1]
    h = x[1] - x[0]
    soma = h / 2 * soma
    return f"Regra dos trapezios generalizada\n{soma}"


def regra_simpson_generalizada(x: list, y: list):
    soma = 0
    index = 0
    h = x[1] - x[0]
    # print((len(y) - 1) / 2)
    for i in range(0, int((len(y) - 1) / 2)):
        soma += h / 3 * (y[index] + y[index + 1] * 4 + y[index + 2])
        # print(i)
        index += 1
    return f"Regra de Simpson Generalizada\n{soma}"


def function(x):
    return math.exp(x) * math.cos(x)


print(
    trapezios_generalizada(
        np.arange(0, 1.4, 0.2), [function(x) for x in np.arange(0, 1.4, 0.2)]
    )
)

print(
    regra_simpson_generalizada(
        np.arange(0, 1.4, 0.2), [function(x) for x in np.arange(0, 1.4, 0.2)]
    )
)
# [1, 1.197, 1.374, 1.503, 1.552, 1.468, 1.202]


# print([function(x) for x in np.arange(0, 1.4, 0.2)])
# print(np.arange(0, 1.2, 0.2))
