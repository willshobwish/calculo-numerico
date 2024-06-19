import math
import numpy as np

def trapezios_generalizada(x: list, y: list):
    soma = 0
    y_soma = y[1 : len(x)-1]
    # print(y_soma)
    for i in y_soma:
        soma += i
    soma = y[0] + (2 * soma) + y[-1]
    h = x[1] - x[0]
    soma = h / 2 * soma
    return f"Regra dos trapezios generalizada\n{soma}"


def regra_simpson_generalizada(x: list, y: list):
    if len(x) != len(y):
        print("Vetores de tamanhos diferentes")
        pass
    soma = 0
    # index = 0
    h = x[1] - x[0]
    # print((len(y) - 1) / 2)
    # print(range(0, int((len(y) - 2)),2))
    for i in range(0, len(y) - 2, 2):
        soma += h / 3 * (y[i] + y[i + 1] * 4 + y[i + 2])
        # print(i)
        # index += 1
    return f"Regra de Simpson um terço\n{soma}"


def tres_oitavo_simpson(x:list, y:list):
    if len(x) != len(y):
        print("Vetores de tamanhos diferentes")
        pass
    soma = 0
    h = x[1]-x[0]
    index=0
    # print(x)
    # print(y)
    for i in range(0, len(y) - 3, 3):
        soma += (h * 3 / 8) * (y[i] + 3 * y[i + 1] + 3 * y[i + 2] + y[i + 3])
    return f"Regra de Simpson três oitavo\n{soma}"

def function(x):
    return math.sqrt(x)
# print(np.arange(1,1.35,0.05))
print(trapezios_generalizada(np.arange(1,1.3,0.05),[function(x) for x in np.arange(1,1.3,0.05)]))
print()
print(regra_simpson_generalizada(np.arange(1,1.3,0.05),[function(x) for x in np.arange(1,1.3,0.05)]))
print()
print(tres_oitavo_simpson(np.arange(1,1.3,0.05),[function(x) for x in np.arange(1,1.3,0.05)]))
# print(np.arange(0,20,5))
print()
print(regra_simpson_generalizada(np.arange(0,25,5),[0,60.6,180.1,341.6,528.4]))
# print()
# print(tres_oitavo_simpson(np.arange(0,25,5),[0,60.6,180.1,341.6,528.4]))