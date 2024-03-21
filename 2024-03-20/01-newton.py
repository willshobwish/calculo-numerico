from numba import jit


def partial_f_partial_x(x:float)->float:
    return 2 * x


def partial_f_partial_y(y:float)->float:
    return 2 * y


def partial_g_partial_x(x:float)->float:
    return 2 * x


def partial_g_partial_y(y:float)->float:
    return -2 * y


def f(x:float, y:float)->float:
    return x**2 + y**2 - 2


def g(x:float, y:float)->float:
    return x**2 - y**2 - 1


def deta(x:float, y:float)->float:
    return partial_f_partial_x(x) * partial_g_partial_y(y) - partial_f_partial_y(
        x
    ) * partial_g_partial_x(x)




xk = 1.2
yk = 1.2
index=0
tolerance = 10**-5
error_x = tolerance*2
error_y = tolerance*2

while index<20 and (error_x>tolerance or error_y>tolerance):
    xk1 = xk + (
        -f(xk, yk) * partial_g_partial_y(yk) + g(xk, yk) * partial_f_partial_y(yk)
    ) / deta(xk, yk)
    yk1 = yk + (
        -g(xk, yk) * partial_f_partial_x(xk) + f(xk, yk) * partial_g_partial_x(xk)
    ) / deta(xk, yk)
    print(f"Iteração={index}\nXk={xk}\nYk={yk}\nError x={error_x}\nError y={error_y}\n")
    error_x = abs(xk1-xk)/abs(xk1)
    error_y = abs(yk1-yk)/abs(yk1)
    xk = xk1
    yk = yk1
    index+=1