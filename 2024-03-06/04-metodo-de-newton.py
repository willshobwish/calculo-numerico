from math import cos, exp, sin, tan, log10, log


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


def question_7a(x):
    return 4 * cos(x) - exp(x)


def derivate_7a(x):
    return -4 * sin(x) - exp(x)


def newton_method(function, derivate, xk, max_iteration, tolerance):
    print(function.__name__)
    index = 0
    error = error1 = error_1 = 1
    while index <= max_iteration and error1 > tolerance:
        xk1 = xk - (function(xk) / derivate(xk))
        error_1 = error
        error = error1
        error1 = abs((xk1 - xk)) / abs(xk1)
        xk = xk1
        print(xk1)
        index += 1

    print(f"P = {log(error1/error)/log(error/error_1)}")
    print()


# xk = 1
# index = 0
# error = 1
# tolerance = 10**-2

newton_method(
    function=function_1,
    derivate=derivate_1,
    xk=1,
    tolerance=10**-4,
    max_iteration=50,
)
newton_method(
    function=function_2,
    derivate=derivate_2,
    xk=1,
    tolerance=10**-4,
    max_iteration=50,
)

newton_method(
    function=function_3,
    derivate=derivate_3,
    xk=1,
    tolerance=10**-4,
    max_iteration=50,
)

newton_method(
    function=function_4,
    derivate=derivate_4,
    xk=-3,
    tolerance=10**-4,
    max_iteration=50,
)
newton_method(
    function=question_7a,
    derivate=derivate_7a,
    xk=0.5,
    tolerance=10**-5,
    max_iteration=50,
)


def question_7b(x):
    return 5 * x**3 + x**2 - 12 * x + 5


def derivate_7b(x):
    return 15 * x**2 + 2 * x - 12


newton_method(
    function=question_7b,
    derivate=derivate_7b,
    xk=0,
    tolerance=10**-5,
    max_iteration=50,
)


def question_7c(x):
    return sin(x) - exp(x)


def derivate_7c(x):
    return cos(x) - exp(x)


newton_method(
    function=question_7c,
    derivate=derivate_7c,
    xk=-4,
    tolerance=10**-5,
    max_iteration=50,
)


def question_7d(x):
    return x**4 - 8


def derivate_7d(x):
    return 4 * x**3

newton_method(
    function=question_7d,
    derivate=derivate_7d,
    xk=1,
    tolerance=10**-5,
    max_iteration=50,
)

