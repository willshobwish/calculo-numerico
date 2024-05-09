# def lagrange_interpolation(x, y, x_val):
#     """
#     Lagrange interpolation function.

#     Parameters:
#     x (list): List of x-coordinates of known points.
#     y (list): List of y-coordinates of known points.
#     x_val (float): The x value where interpolation is to be computed.

#     Returns:
#     float: Interpolated y value corresponding to x_val.
#     """
#     n = len(x)
#     result = 0.0
#     for i in range(n):
#         term = y[i]
#         for j in range(n):
#             if j != i:
#                 term *= (x_val - x[j]) / (x[i] - x[j])
#         result += term
#     return result

# # Example usage:
# x = [0.1, 0.2, 0.3]
# y = [0.1349, 0.3644, 0.7378]
# x_val = 0.25
# interpolated_y = lagrange_interpolation(x, y, x_val)
# print("Interpolated value at x =", x_val, "is", interpolated_y)


def pi(val, x):
    result = 1
    for i in x:
        result = result * (val - i)
    return result


def lagrange(val, x, y):
    pi = pi_derivate = 1
    s = 0
    for i in range(len(x)):
        pi *= val - x[i]
    print(f"Pi: {pi}")
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                pi_derivate *= x[i] - x[j]
        dk = (val - x[i]) * pi_derivate
        s += y[i] / dk
        pi_derivate = 1
    print(f"s: {s}")
    return pi * s


print(lagrange(0.25, [0.1, 0.2, 0.3], [0.1349, 0.3644, 0.7378]))
