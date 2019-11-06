from lab1_1 import *
from lab1_2 import *

def f_multi(x):
    return x[0] ** 2 + x[1] ** 2

def g(f, x0, vector, lbd):
    return f([x0[i] + lbd * vector[i] for i in range(len(x0))])

x0 = [5, 5]
vector = [-1, -1]

def g_simplified(lbd):
    return g(f_multi, x0, vector, lbd)

find_minimum_fibonacci(g_simplified, 0.01, *find_minimum_interval(g_simplified, 0, 0.01))
