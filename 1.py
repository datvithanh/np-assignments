import numpy as np

def my_sqrt(x):
    if (x <= 0):
        return 0
    x, exp = np.frexp(x)
    if (exp & 1):
        exp-=1
        x *= 2
    y = (1+x)/2
    z = 0
    while (y != z):
        z = y
        y = (y + x/y) / 2
    return y * 2**(exp/2)

print(my_sqrt(3.5))
