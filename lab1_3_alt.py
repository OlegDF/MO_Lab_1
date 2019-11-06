from lab1_1_alt import *
from lab1_2 import *

def g(f, x0, vector, lbd):
    return f([x0[i] + lbd * vector[i] for i in range(len(x0))])
