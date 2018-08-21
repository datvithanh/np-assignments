import math
import numpy as np 

"""
Theo clt thuc hien vo han lan tung 5 xx va lay tong.
Tap hop ay tuan theo phan phoi chuan.
Tim mean, variance cua tung 5 xx roi ap cong thuc pdf cua phan phoi chuan
"""

def normal_distribution_pdf(mean, var, x):
    return np.exp( -(mean - x)**2 / (2 * var)) / np.sqrt(2 * math.pi * var)

def one_dice_var():
    sum = 0
    for i in range(1,7):
        print(i)
        sum = sum + 1/6 * (3.5 - i * 1.0) ** 2
    return sum

print(normal_distribution_pdf(5 * 3.5, 5 * one_dice_var(), 17))