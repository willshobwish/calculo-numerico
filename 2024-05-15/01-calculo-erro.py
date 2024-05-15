import math
import numpy as np

def function_1(x):
    return x * math.exp(3 * x)


def diff_fun_1(x):
    return 27 * math.exp(3 * x) + 27 * x * math.exp(3 * x)


def error(x: float, x_array: list, n: int, t: float, diff_fun):
    pi = 1
    for item in x_array:
        pi *= abs(x - item)
    pi_factorial = pi / math.factorial(n + 1)
    print(pi_factorial)
    print(np.around(pi_factorial,6))
    print(diff_fun(t))
    pi_factorial = pi_factorial * abs(diff_fun(t))
    return pi_factorial


print(error(0.25, [0.1, 0.2, 0.3], 2, 0.3, diff_fun_1))
