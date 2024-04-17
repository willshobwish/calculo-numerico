from math import sqrt, log10


def function_1(x):
    return sqrt(x + 2)


x = 2.2
tolerance = 10**-3
error = 1
iteration = 0
xbar = 2
while error > tolerance and iteration < 10:
    new_x = function_1(x)
    xp1 = abs(function_1(new_x))
    error = abs((new_x - x)) / abs(new_x)

    errork1 = abs(xp1 - xbar)
    error_k1 = abs(x - 2)
    x = new_x
    p = log10(errork1 / error) / log10(error / error_k1)
    print(new_x, p)
    iteration += 1
