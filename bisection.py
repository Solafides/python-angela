import math

def f(x):
    return math.exp(-x) - x

def bisection_method(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    c = a
    while (b - a) > tolerance:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# Define the interval and tolerance
a = 0
b = 1
tolerance = 0.015

# Find the root
root = bisection_method(a, b, tolerance)
print(f"The root is approximately at x = {root}")
