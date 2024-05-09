import math


def function_1(x):
    return math.sqrt(x) - 5 * math.exp(-x)


def function_2(x):
    return -2.7 * math.log(x)


def function_3(x):
    return math.log10(x) - math.cos(x)


def function_4(x):
    return math.exp(-x) - math.log10(x)


def question_10(x):
    return math.sqrt(x) - 5 * math.exp(-x)


def question_11a(x):
    return -2.7 * math.log(x) - x


def question_11b(x):
    return math.log10(x) - math.cos(x)


def question_11c(x):
    return math.exp(-x) - math.log10(x)


def secant_method(function, xk, xk_1, tolerance, max_iteration):
    error1 = error_1 = error = 10 * tolerance
    index = 0
    print(f"{function.__name__}")
    while error > tolerance and index < max_iteration:
        xk1 = (xk_1 * function(xk) - xk * function(xk_1)) / (
            function(xk) - function(xk_1)
        )

        error_1 = error
        error = error1
        error1 = abs(xk1 - xk) / abs(xk1)

        xk_1 = xk
        xk = xk1
        print(f"Raiz: {xk}")
    convergence = math.log10(error1 / error) / math.log10(error / error_1)
    print(f"Convergencia: {convergence}\n")


# secant_method(
#     function=function_1, xk=1.4, xk_1=1.5, tolerance=10**-2, max_iteration=100
# )

# secant_method(function=function_2, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100)

# secant_method(function=function_3, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100)

# secant_method(function=function_4, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100)

secant_method(
    function=question_10, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100
)

secant_method(
    function=question_11a, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100
)

secant_method(
    function=question_11b, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100
)

secant_method(
    function=question_11c, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100
)


# secant_method(
#     function=question_10, xk=1, xk_1=1.25, tolerance=10**-4, max_iteration=100
# )
