import math


def function_1(x):
    return math.sqrt(x + 2)


def question_1(x):
    return math.exp(x)/4


def question_2(x):
    return 2 * x * x - 5 * x + 2


def iteracao_linear(function, x, x_1, xbar, tolerance, error, max_iteration, files):
    iteration = 0
    resultados = []
    while error > tolerance and iteration < max_iteration:
        x = function(x_1)
        x1 = function(x)
        error = abs(x - x_1) / abs(x)
        error2 = abs(x1 - xbar)
        error1 = abs(x - xbar)
        error_1 = abs(x_1 - xbar)
        p = math.log(error2 / error1) / math.log(error1 / error_1)
        print(f"{x} {p}")
        resultados.append(x)
        x_1 = x
        x = x1
        iteration += 1

    string_array = [str(element) for element in resultados]
    with open(f"{files}", "w") as file_file:
        file_file.write("\n".join(string_array))


iteracao_linear(
    function=question_1,
    x=0,
    x_1=1,
    xbar=2,
    tolerance=10**-2,
    error=1,
    max_iteration=20,
    files="Questão 1_1.txt",
)
iteracao_linear(
    function=question_1,
    x=2,
    x_1=4,
    xbar=2,
    tolerance=10**-2,
    error=1,
    max_iteration=20,
    files="Questão 1_2.txt",
)
iteracao_linear(
    function=question_2,
    x=0.4,
    x_1=2,
    xbar=5,
    tolerance=10**-2,
    error=1,
    max_iteration=20,
    files="Questão 2.txt",
)
