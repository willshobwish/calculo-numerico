# def partial_f_partial_x(x: float) -> float:
#     return 2 * x


# def partial_f_partial_y(y: float) -> float:
#     return 2 * y


# def partial_g_partial_x(x: float) -> float:
#     return 2 * x


# def partial_g_partial_y(y: float) -> float:
#     return -2 * y


# def f(x: float, y: float) -> float:
#     return x**2 + y**2 - 2


# def g(x: float, y: float) -> float:
#     return x**2 - y**2 - 1


def deta(
    x: float,
    y: float,
    partial_f_partial_x,
    partial_g_partial_y,
    partial_f_partial_y,
    partial_g_partial_x,
) -> float:
    return partial_f_partial_x(x, y) * partial_g_partial_y(x, y) - partial_f_partial_y(
        x, y
    ) * partial_g_partial_x(x, y)


# xk = 1.2
# yk = 1.2
# index = 0
# tolerance = 10**-5
# error_x = tolerance * 2
# error_y = tolerance * 2


def newton(
    max_iter,
    tolerance,
    xk,
    yk,
    function_f,
    function_g,
    partial_f_partial_x,
    partial_g_partial_y,
    partial_f_partial_y,
    partial_g_partial_x,
):
    error_x = error_y = 1
    index = 0
    while index < max_iter and (error_x > tolerance or error_y > tolerance):
        xk1 = xk + (
            -function_f(xk, yk) * partial_g_partial_y(xk, yk)
            + function_g(xk, yk) * partial_f_partial_y(xk, yk)
        ) / deta(
            xk,
            yk,
            partial_f_partial_x,
            partial_g_partial_y,
            partial_f_partial_y,
            partial_g_partial_x,
        )
        yk1 = yk + (
            -function_g(xk, yk) * partial_f_partial_x(xk, yk)
            + function_f(xk, yk) * partial_g_partial_x(xk, yk)
        ) / deta(
            x=xk,
            y=yk,
            partial_f_partial_x=partial_f_partial_x,
            partial_f_partial_y=partial_f_partial_y,
            partial_g_partial_x=partial_g_partial_x,
            partial_g_partial_y=partial_g_partial_y
        )
        print(
            f"Iteração={index}\nFuncao: {function_f.__name__} {function_g.__name__}\nXk={xk}\nYk={yk}\nError x={error_x}\nError y={error_y}\n"
        )
        error_x = abs(xk1 - xk) / abs(xk1)
        error_y = abs(yk1 - yk) / abs(yk1)
        xk = xk1
        yk = yk1
        index += 1


def question_17_a_pf_px(x, y):
    return 6 * x * y


def question_17_a_pg_px(x, y):
    return 2 * x + y**3


def question_17_a_pf_py(x, y):
    return 3 * x**2 - 3 * y**2


def question_17_a_pg_py(x, y):
    return 3 * x * y**2


def question_17_a_f(x, y):
    return 3 * x**2 * y - y**3 - 4


def question_17_a_g(x, y):
    return x**2 + x * y**3 - 9


newton(
    100,
    10**-3,
    -1,
    -2,
    question_17_a_f,
    question_17_a_g,
    question_17_a_pf_px,
    question_17_a_pg_px,
    question_17_a_pf_py,
    question_17_a_pg_py,
)


def question_17_b_pf_px(x, y):
    return 2 * x


def question_17_b_pg_px(x, y):
    return 2 * x


def question_17_b_pf_py(x, y):
    return 2 * y


def question_17_b_pg_py(x, y):
    return 2 * y


def question_17_b_f(x, y):
    return x**2 + y**2 - 1


def question_17_b_g(x, y):
    return x**2 + y**2 + 0.5


# newton(
#     tolerance=10**-3,
#     max_iter=100,
#     xk=0.4,
#     yk=0.9,
#     function_f=question_17_b_f,
#     function_g=question_17_b_g,
#     partial_f_partial_x=question_17_b_pf_px,
#     partial_f_partial_y=question_17_b_pf_py,
#     partial_g_partial_x=question_17_b_pg_px,
#     partial_g_partial_y=question_17_b_pg_py,
# )


def question_17_c_pf_px(x, y):
    return 2 * x - 2


def question_17_c_pg_px(x, y):
    return 2 * x


def question_17_c_pf_py(x, y):
    return 2 * y


def question_17_c_pg_py(x, y):
    return 2 * y - 2


def question_17_c_f(x, y):
    return x**2 + y**2 - 2 * x - 3


def question_17_c_g(x, y):
    return x**2 + y**2 - 2 * y - 3


newton(
    tolerance=10**-3,
    max_iter=100,
    xk=2,
    yk=1,
    function_f=question_17_c_f,
    function_g=question_17_c_g,
    partial_f_partial_x=question_17_c_pf_px,
    partial_f_partial_y=question_17_c_pf_py,
    partial_g_partial_x=question_17_c_pg_px,
    partial_g_partial_y=question_17_c_pg_py,
)
