import math


# def function_1(x):
#     return math.sqrt(x + 2)


def question_1(x):
    return math.exp(x) / 4


def question_2_a(x):
    return 2*x*x+2/5

def question_2_b(x):
    return math.sqrt((5*x/2)-1)

def iteracao_linear(function, x_1, xbar, tolerance, error, max_iteration):
    iteration = 0

    while error > tolerance and iteration < max_iteration:
        x = function(x_1)
        x1 = function(x)
        error = abs(x - x_1) / abs(x)
        error2 = abs(x1 - xbar)
        error1 = abs(x - xbar)
        error_1 = abs(x_1 - xbar)

        print(f"Raiz: {x}")
        x_1 = x
        x = x1
        iteration += 1
    p = math.log(error2 / error1) / math.log(error1 / error_1)
    print(f"Convergencia: {p}")


# iteracao_linear(
#     function=question_1,
#     x_1=1,
#     xbar=2,
#     tolerance=10**-2,
#     error=1,
#     max_iteration=20,
# )
# iteracao_linear(
#     function=question_1,
#     x_1=0,
#     xbar=1,
#     tolerance=10**-2,
#     error=1,
#     max_iteration=20,
# )

# iteracao_linear(
#     function=question_1,
#     x_1=1.5,
#     xbar=3,
#     tolerance=10**-2,
#     error=1,
#     max_iteration=20,
# )

iteracao_linear(
    function=question_2_a,
    x_1=0.5,
    xbar=2,
    tolerance=10**-5,
    error=1,
    max_iteration=20,
)
iteracao_linear(
    function=question_2_b,
    x_1=0.5,
    xbar=2,
    tolerance=10**-5,
    error=1,
    max_iteration=20,
)