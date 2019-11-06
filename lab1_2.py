import sys

def find_minimum_interval(f, x0, eps):
    x_previous = x0
    f_previous = f(x0)
    f_greater = f(x0 + eps / 3)
    if(f_previous > f_greater):
       x_current = x0 + eps / 3
       f_current = f_greater
       h = eps / 3
    else:
        f_lesser = f(x0 - eps / 3)
        if(f_previous > f_lesser):
            x_current = x0 - eps / 3
            f_current = f_lesser
            h = -eps / 3
        else:
            return x0, x0
    while(h < sys.float_info.max / 2):
        h *= 2
        x_future = x_current + h
        if(f(x_current) > f(x_future)):
            x_previous = x_current
            x_current = x_future
        elif x_previous < x_future:
            return x_previous, x_future
        else:
            return x_future, x_previous

def f1(x):
    return x ** 2
