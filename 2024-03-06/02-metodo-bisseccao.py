import math


def function_1(x):
    return x**2 + 2 * x + 1


def function_2(x):
    return x**3 + 3 * x - 1


def function_3(x):
    return x**2 - math.sin(x)


def bissection_method(function, a, b, max_index):
    index = 0
    while index <= max_index:
        x = (a + b) / 2
        fa = function(a)
        # fb = function(b)
        fx = function(x)
        if fx * fa < 0:
            b = x
            # fb = function(b)
        else:
            a = x
            fa = function(a)
        print(
            f"Function: {function.__name__}\nIteration: {index}\nf(x): {fx}\nx: {x}\n"
        )
        index += 1


bissection_method(function=function_1, a=-2, b=0, max_index=10)
bissection_method(function=function_2, a=0, b=1, max_index=10)
bissection_method(function=function_3, a=0.5, b=1, max_index=10)
