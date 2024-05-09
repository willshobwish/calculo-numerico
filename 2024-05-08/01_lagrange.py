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
