from lab1_1_alt import *
from lab1_3_alt import *

def gradient(f_multi, x):
    global f_calls
    grad = []
    grad.append(-400 * x[1] * x[0] + 400 * x[0] ** 3 - 2 + 2 * x[0])
    grad.append(200 * x[1] - 200 * x[0] ** 2)
    f_calls += 1
    return grad

def normalized_gradient(f_multi, x):
    grad = gradient(f_multi, x)
    length = 0
    for i in range(len(grad)):
        length += grad[i] ** 2
    length = math.sqrt(length)
    if(length > 1):
        for i in range(len(grad)):
            grad[i] /= length
    return grad

def g_simplified(lbd):
    global x_current
    return g(f_chosen, x_current, normalized_gradient(f_chosen, x_current), lbd)

def g_canyon(lbd):
    global x_canyon, vector_canyon
    return g(f_chosen, x_canyon, vector_canyon, lbd)

def lbd(x):
    return find_minimum_fibonacci(g_simplified, 0.00001, *find_minimum_interval(g_simplified, 0, 0.00001))

def lbd_canyon():
    return find_minimum_fibonacci(g_canyon, 0.00001, *find_minimum_interval(g_canyon, 0, 0.00001))

def descend(f_multi, eps, x_starting):
    global x_current, x_canyon, vector_canyon, f_calls
    x_list = []
    x_list.append(x_starting.copy())
    f_calls = 0
    iteration = 1
    x_previous = x_starting
    x_current = x_starting.copy()
    x_list.append(x_current.copy())
    lbd_current = lbd(x_current) / 2
    grad = normalized_gradient(f_multi, x_previous)
    x_current = [x_previous[i] + lbd_current * grad[i] for i in range(len(x_previous))]
    slow_steps = 0
    canyon_steps = 0
    while(slow_steps <= 4):
        lbd_current = lbd(x_current)
        x_previous = x_current.copy()
        grad = normalized_gradient(f_multi, x_previous)
        x_current = [x_previous[i] + lbd_current * grad[i] for i in range(len(x_previous))]
        if(distance(x_previous, x_current) <= eps * 10 and canyon_steps >= 3):
            x_canyon = x_list[len(x_list) - 2]
            vector_canyon = [x_current[i] - x_canyon[i] for i in range(len(x_canyon))]
            lbd_current = lbd_canyon()
            x_current = [x_canyon[i] + vector_canyon[i] * lbd_current for i in range(len(x_canyon))]
            if(distance(x_previous, x_current) > eps):
                canyon_steps = 0
                slow_steps = 0
        x_list.append(x_current.copy())
        iteration += 1
        if(distance(x_previous, x_current) <= eps * 10):
            canyon_steps += 1
        if(distance(x_previous, x_current) <= eps):
            slow_steps += 1
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

"""f_num = int(input("Введите номер функции: "))
eps = float(input("Введите точность: "))"""
f_num = 1
eps = 0.00001
print("Введите стартовую позицию: ")
x_starting = [float(x) for x in input().split()]
f_chosen = functions[f_num - 1]
res = descend(f_chosen, eps, x_starting)
print(res)
print(f_chosen(res))

