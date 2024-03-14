# import matplotlib.pyplot as plt
# import numpy
def f(x):
    return x * x + 2 * x + 1


i = 0
a = -2
b = 5

while i < 40:
    x = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fx = f(x)
    if fx * fa < 0:
        b = x
        fb = f(b)
    else:
        a = x
        fa = f(a)
    print(f"{fx}\n{fa}\n{fb}\n{x}")
    i += 1
