from math import cos, exp, sin


def f(x):
    return 4 * cos(x) - exp(x)


def f_derivate(x):
    return -4 * sin(x) - exp(x)


xk = 1
i = 0
error = 1
tolerance = 10**-2
while i <= 10 and error > tolerance:
    xk1 = xk - (f(xk) / f_derivate(xk))
    error = abs((xk1 - xk)) / abs(xk1)
    xk = xk1
    print(xk1)
    i += 1
