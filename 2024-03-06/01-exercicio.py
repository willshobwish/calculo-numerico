# import matplotlib.pyplot as plt
# import numpy
i = 0
a = -2
b = 5
# old = 1000
while i < 40:
    x = (a+b)/2
    fa = a*a+2*a+1
    fb = b*b+2*b+1
    fx = x*x+2*x+1
    if fx * fa < 0:
        b = x
        fb = b*b+2*b+1
    else:
        a = x
        fa = a*a+2*a+1
    print(f'{fx}\n{fa}\n{fb}\n{x}')
    i += 1
