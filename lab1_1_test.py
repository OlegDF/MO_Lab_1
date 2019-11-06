import math
from lab1_1 import *

def f1(x):
    return math.sin(x)

def f2(x):
    return math.cos(x)

def f3(x):
    return (x - 2) ** 2

def f4(x):
    return (x - 15) ** 2 + 5

def f5(x):
    return (x + 5) ** 4

def f6(x):
    return math.exp(x)

def f7(x):
    return x ** 2 + 2 * x - 4

def f8(x):
    return x ** 3 - x

functions = [f1, f2, f3, f4, f5, f6, f7, f8]
borders = [
    [-math.pi / 2, math.pi / 2],
    [0, math.pi],
    [-2, 20],
    [2, 200],
    [-10, 15],
    [0, 100],
    [-10, 20],
    [0, 1],
]

f_num = int(input("Введите номер функции: "))
eps = float(input("Введите точность: "))
find_minimum_dichotomy(functions[f_num - 1], eps, borders[f_num - 1][0], borders[f_num - 1][1])
find_minimum_golden(functions[f_num - 1], eps, borders[f_num - 1][0], borders[f_num - 1][1])
find_minimum_fibonacci(functions[f_num - 1], eps, borders[f_num - 1][0], borders[f_num - 1][1])
