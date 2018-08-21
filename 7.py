import numpy as np

def cal(sunny, rainy):
    return sunny*0.3 + rainy * 0.6, sunny*0.7 + rainy*0.4
def simulate(days = 7):
    sunny = 0.5
    rainy = 0.5

    for i in range(days):
        sunny, rainy = cal(sunny, rainy)
    
    return sunny, rainy

print(simulate(7))