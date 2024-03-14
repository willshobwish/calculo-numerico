def function(x):
    return x**3 + 3 * x - 1


a = 0
b = 1
i = 0
while i <= 10:
    x = (a + b) / 2
    fa = function(a)
    fb = function(b)
    fx = function(x)
    if fx * fa < 0:
        b = x
        fb = function(b)
    else:
        a = x
        fa = function(a)
    print(f"Iteração: {i}\nFX: {fx}\nX: {x}\n\n")
    i += 1
