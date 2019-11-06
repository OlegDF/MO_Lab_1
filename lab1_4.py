from lab1_1_alt import *
from lab1_3_alt import *

def gradient(f_multi, x):
    grad = []
    h = 0.0001
    for i in range(len(x)):
        first = x.copy()
        second = x.copy()
        first[i] += h
        second[i] -= h
        grad.append((f_multi(first) - f_multi(second)) / (2 * h))
    return grad

def g_simplified(lbd):
    global x_current
    return g(f_chosen, x_current, gradient(f_chosen, x_current), lbd)

def lbd(x):
    return find_minimum_fibonacci(g_simplified, 0.0001, *find_minimum_interval(g_simplified, 0, 0.0001))

def descend(f_multi, eps, x_starting):
    global x_current, f_calls
    f_calls = 0
    iteration = 1
    x_previous = x_starting
    x_current = x_starting.copy()
    lbd_current = lbd(x_previous)
    x_current = [x_current[i] - lbd_current * (-gradient(f_multi, x_current)[i]) for i in range(len(x_current))]
    while(distance(x_previous, x_current) > eps):
        lbd_current = lbd(x_current)
        x_previous = x_current.copy()
        x_current = [x_previous[i] - lbd_current * (-gradient(f_multi, x_previous)[i]) for i in range(len(x_previous))]
        iteration += 1
    print("Число итераций:", iteration)
    print("Число вызовов функции:", f_calls)
    return x_current

def distance(v1, v2):
    return math.sqrt(sum([(v1[i] - v2[i]) ** 2 for i in range(len(x_current))]))

def f1(x):
    global f_calls
    f_calls += 1
    ans = 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    return ans

def f2(x):
    global f_calls
    f_calls += 1
    ans = (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    return ans

def f3(x):
    global f_calls
    f_calls += 1
    ans = (x[1] - x[0]) ** 2 + 100 * (1 - x[0]) ** 2
    return ans

def f4(x):
    global f_calls
    f_calls += 1
    ans = 100 * (x[1] - x[0] ** 3) ** 2 + (1 - x[0]) ** 2
    return ans

def f5(x):
    global f_calls
    f_calls += 1
    ans = (1.5 - x[0] * (1 - x[1])) ** 2 + (2.25 - x[0] * (1 - x[1]) ** 2) ** 2 + (2.625 - x[0] * (1 - x[1]) ** 3) ** 2
    return ans

def f6(x):
    global f_calls
    f_calls += 1
    ans = 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2 + 90 * (x[3] - x[2] ** 2) + (1 - x[2]) ** 2 + 10.2 * (x[1] - 1) ** 2 + (x[3] - 1) ** 2 + 19.8 * (x[1] - 1) * (x[3] - 1)
    return ans

def f7(x):
    global f_calls
    f_calls += 1
    ans = (x[1] - x[0]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4
    return ans

functions = [f1, f2, f3, f4, f5, f6, f7]
dimensions = [2, 2, 2, 2, 2, 4, 4]

f_num = int(input("Введите номер функции: "))
eps = float(input("Введите точность: "))
print("Введите стартовую позицию: ")
x_starting = [float(x) for x in input().split()]
f_chosen = functions[f_num - 1]
res = descend(f_chosen, eps, x_starting)
print(res)
print(f_chosen(res))

