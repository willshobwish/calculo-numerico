import math
import numpy as np


def del_f_del_x(x, y):
    return 2 * 0.2 * x + 0.2 * y


def del_f_del_y(x, y):
    return 0.2 * x


def del_g_del_x(x, y):
    return 0.4 + 0.1 * y**2


def del_g_del_y(x, y):
    return 2 * 0.1 * x * y


x = 0.9
y = 0.8
print(del_f_del_x(x, y))
print(del_f_del_y(x, y))
print(str(abs(del_f_del_x(x, y)) + abs(del_f_del_y(x, y))) + "\n")

print(del_g_del_x(x, y))
print(del_g_del_y(x, y))
print(abs(del_g_del_x(x, y)) + abs(del_g_del_y(x, y)))
