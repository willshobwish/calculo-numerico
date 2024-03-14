import math


def function(x):
    return math.sqrt(x) - 5 * math.exp(-x)


xk = 1
xk_1 = 1.25
tolerance = 10**-10
error = 10 * tolerance
cont = 1
max_iteration = 100
while error > tolerance and cont < max_iteration:
    xk1 = (xk_1 * function(xk) - xk * function(xk_1)) / (function(xk) - function(xk_1))
    error = abs(xk1 - xk) / abs(xk1)
    xk_1 = xk
    xk = xk1
    print(xk)
