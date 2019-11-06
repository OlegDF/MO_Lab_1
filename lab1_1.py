import math

sqrt_5 = math.sqrt(5)
iteration = 0
f_calls = 0

def find_minimum(first_search, border_search, f, eps, a, b):
    global iteration, f_calls
    if(b - a < eps):
        print("Число итераций:", iteration)
        print("Число вызовов функции:", f_calls)
        iteration = 0
        f_calls = 0
        return (a + b) / 2
    else:
        if(iteration == 0):
            x1, x2, f_x1, f_x2 = first_search(f, eps, a, b)
        else:
            x1, x2, f_x1, f_x2 = border_search(f, eps, a, b)
        print(a, b, x1, x2)
        print("f ", f(a), f(b), f(x1), f(x2))
        iteration += 1
        if(f_x1 < f_x2):
            return find_minimum(first_search, border_search, f, eps, a, x2)
        elif(f_x1 > f_x2):
            return find_minimum(first_search, border_search, f, eps, x1, b)
        else:
            return find_minimum(first_search, border_search, f, eps, x1, x2)

def find_minimum_dichotomy(f, eps, a, b):
    print("Метод дихотомии:")
    print("Минимум:", find_minimum(dichotomy_borders, dichotomy_borders, f, eps, a, b))

def dichotomy_borders(f, eps, a, b):
    global f_calls
    f_calls += 2
    x1 = (a + b) / 2 - eps / 3
    x2 = (a + b) / 2 + eps / 3
    return x1, x2, f(x1), f(x2)

def find_minimum_golden(f, eps, a, b):
    print("Метод золотого сечения:")
    print("Минимум:", find_minimum(golden_borders_first, golden_borders, f, eps, a, b))

def golden_borders_first(f, eps, a, b):
    global f_calls
    f_calls += 2
    global x_cache, f_cache
    x1 = a + (3 - sqrt_5) / 2 * (b - a)
    x2 = a + (sqrt_5 - 1) / 2 * (b - a)
    f_x1 = f(x1)
    f_x2 = f(x2)
    if(f_x1 < f_x2):
        x_cache = x1
        f_cache = f_x1
    else:
        x_cache = x2
        f_cache = f_x2
    return x1, x2, f_x1, f_x2

def golden_borders(f, eps, a, b):
    global x_cache, f_cache, f_calls
    x1 = a + (3 - sqrt_5) / 2 * (b - a)
    x2 = a + (sqrt_5 - 1) / 2 * (b - a)
    if(abs(x1 - x_cache) <= eps / 1000):
        f_x1 = f_cache
        f_x2 = f(x2)
        f_calls += 1
    elif(abs(x2 - x_cache) <= eps / 1000):
        f_x1 = f(x1)
        f_x2 = f_cache
        f_calls += 1
    else:
        f_x1 = f(x1)
        f_x2 = f(x2)
        f_calls += 2
    if(f_x1 < f_x2):
        x_cache = x1
        f_cache = f_x1
    else:
        x_cache = x2
        f_cache = f_x2
    return x1, x2, f_x1, f_x2

def find_minimum_fibonacci(f, eps, a, b):
    print("Метод Фибоначчи:")
    initialize_fibonacci_numbers(eps, a, b)
    print("Минимум:", find_minimum(fibonacci_borders_first, fibonacci_borders, f, eps, a, b))

def initialize_fibonacci_numbers(eps, a, b):
    global fibonacci, n
    n = -1
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)
    while(fibonacci[n + 2] <= (b-a) / eps):
        fibonacci.append(fibonacci[n + 1] + fibonacci[n + 2])
        n += 1

def fibonacci_borders_first(f, eps, a, b):
    global f_calls
    f_calls += 2
    global x_cache, f_cache, k
    k = 1
    x1 = a + fibonacci[n] / fibonacci[n + 2] * (b - a)
    x2 = a + fibonacci[n + 1] / fibonacci[n + 2] * (b - a)
    f_x1 = f(x1)
    f_x2 = f(x2)
    if(f_x1 < f_x2):
        x_cache = x1
        f_cache = f_x1
    else:
        x_cache = x2
        f_cache = f_x2
    return x1, x2, f_x1, f_x2

def fibonacci_borders(f, eps, a, b):
    global x_cache, f_cache, f_calls, k
    k += 1
    x1 = a + fibonacci[n - k + 1] / fibonacci[n - k + 3] * (b - a)
    x2 = a + fibonacci[n - k + 2] / fibonacci[n - k + 3] * (b - a)
    if(abs(x1 - x_cache) <= eps / 1000):
        f_x1 = f_cache
        f_x2 = f(x2)
        f_calls += 1
    elif(abs(x2 - x_cache) <= eps / 1000):
        f_x1 = f(x1)
        f_x2 = f_cache
        f_calls += 1
    else:
        f_x1 = f(x1)
        f_x2 = f(x2)
        f_calls += 2
    if(f_x1 < f_x2):
        x_cache = x1
        f_cache = f_x1
    else:
        x_cache = x2
        f_cache = f_x2
    return x1, x2, f_x1, f_x2

