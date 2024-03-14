import matplotlib.pyplot as plt
import numpy as np
import math


def function(x):
    return math.sqrt(x) - 5 * math.exp(-x)


quantity = 100000
array = np.arange(1, quantity + 1, 1)
array_function = [function(i) for i in array]
# array_function_2 = [i**2 for i in array]
# print(array)
plt.plot(array, array_function)
array_i = np.full((1, quantity), 0)[0]
plt.plot(array, array_i)
# plt.plot(array, array_function_2)
plt.show()
