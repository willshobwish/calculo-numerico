import math


def function_1(x):
    return math.sqrt(x) - 5 * math.exp(-x)


def regula_falsi(function, xk, xk_1, tolerance, max_iteration):

    error = error_1 = error1 = 1
    cont = 1
    print(function.__name__)
    while error > tolerance and cont < max_iteration:
        error_1 = error
        error = error1
        xk1 = (xk_1 * function(xk) - xk * function(xk_1)) / (
            function(xk) - function(xk_1)
        )

        error1 = abs(xk1 - xk) / abs(xk1)
        if function(xk) * function(xk_1) < 0:
            xk_1 = xk
            xk = xk1
        else:
            xk = xk1

        print(f"{xk}")
    convergence = math.log10(error1 / error) / math.log10(error / error_1)
    print(f"Convergencia: {convergence}\n")


# xk = 1
# xk_1 = 2
# tolerance = 10**-10
# max_iteration = 100


def question_12(x):
    return x - math.cos(x)


def question_13a(x):
    return math.sin(x) - x * math.exp(x)


def question_13b(x):
    return math.cos(x) * math.exp(x)


def question_14(x):
    return x - 2 * math.sin(x)


regula_falsi(function=function_1, xk=0, xk_1=0.5, tolerance=10**-4, max_iteration=40)
regula_falsi(function=question_12, xk=-1, xk_1=1, tolerance=10**-5, max_iteration=40)
regula_falsi(function=question_13a, xk=-4, xk_1=3, tolerance=10**-5, max_iteration=40)
regula_falsi(function=question_13b, xk=-2, xk_1=-1, tolerance=10**-5, max_iteration=40)
regula_falsi(function=question_14, xk=1.8, xk_1=3, tolerance=10**-3, max_iteration=40)
