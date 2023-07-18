import numpy as np
import math


def f(x):
    return x**2 - 1.5*x

epsilon = 0.01
a = 0
b = 1
x1 = a
x2 = b
while (abs(a-b) > (2*epsilon)):
    x1 = (a + b - epsilon)/2
    x2 = (a + b + epsilon)/2
    f1 = f(x1)
    f2 = f(x2)
    if (f1 < f2):
        b = x2
    elif (f1 > f2):
        a = x1
    else:
        a = x1
        b = x2
    print(f'(a, b) = ({a:.4f}, {b:.4f})')

print(f"epsilon = {epsilon:.4f}")
print(f"x = {x1:.4f}")
print(f"f(x) min = {f(x1):.4f}")
