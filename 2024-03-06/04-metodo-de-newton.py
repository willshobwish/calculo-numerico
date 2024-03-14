from math import cos, exp, sin


def function(x):
    return 4*cos(x)-exp(x)


def function_derivate(x):
    return -4*sin(x)-exp(x)


xk = 1
i = 0
error = 1
tolerance = 10**-2
while i <= 10 and error > tolerance:
    xk1 = xk-(function(xk)/function_derivate(xk))
    error = abs((xk1-xk))/abs(xk1)
    xk = xk1
    print(xk1)
    i += 1
