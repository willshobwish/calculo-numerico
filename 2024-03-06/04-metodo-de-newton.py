from math import cos, exp, sin, tan


def sec(x):
    return 1 / cos(x)


def function_1(x):
    return 4 * cos(x) - exp(x)


def derivate_1(x):
    return -4 * sin(x) - exp(x)


def function_2(x):
    return tan(x) - 2 * x


def derivate_2(x):
    return sec(x) ** 2 - 2


def function_3(x):
    return 5 * x**3 + x**2 - 12 * x + 5


def derivate_3(x):
    return 15 * x**2 + 2 * x - 12


def function_4(x):
    return sin(x) - exp(x)


def derivate_4(x):
    return cos(x) - exp(x)


def newton_method(function, derivate, xk, index, error, tolerance):
    print(function.__name__)
    while index <= 10 and error > tolerance:
        xk1 = xk - (function(xk) / derivate(xk))
        error = abs((xk1 - xk)) / abs(xk1)
        xk = xk1
        print(xk1)
        index += 1
    print()


# xk = 1
# index = 0
# error = 1
# tolerance = 10**-2

newton_method(
    function=function_1, derivate=derivate_1, xk=1, index=0, error=1, tolerance=10**-4
)
newton_method(
    function=function_2, derivate=derivate_2, xk=1, index=0, error=1, tolerance=10**-4
)

newton_method(
    function=function_3, derivate=derivate_3, xk=1, index=0, error=1, tolerance=10**-4
)

newton_method(
    function=function_4, derivate=derivate_4, xk=-3, index=0, error=1, tolerance=10**-4
)
