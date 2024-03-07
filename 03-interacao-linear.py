from math import sqrt, log10


def function_1(x):
    return sqrt(x+2)


old_x = 2.2
tolerance = 0.001
error = 1
iteration = 0
x_ = 2
while error > tolerance and iteration < 10:
    new_x = function_1(old_x)
    x_new_plus_1 = abs(function_1(new_x))
    error = abs((new_x-old_x))/abs(new_x)

    error_k1 = abs(x_new_plus_1-x_)
    error_k_minus_1 = abs(old_x-2)
    old_x = new_x
    p = log10(error_k1/error)/log10(error/error_k_minus_1)
    print(new_x, p)
    iteration += 1
