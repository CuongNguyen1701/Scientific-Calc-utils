import math
def f(x):
    return math.sin(x) - (x**2)*math.cos(x)
# Tìm nghiệm gần đúng của phương trình 5x^3 - x^2 - x - 1 = 0
a = -0.5
b = 2
tolerance = 0.001

def bisection_method(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("Khong ap dung duoc phuong phap chia doi trong khoang nay.")
        return None

    while (b - a) >= tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


approx_solution = bisection_method(a, b, tolerance)
if approx_solution is not None:
    print("Nghiem gan dung:", approx_solution)
else:
    print("Khong tim thay nghiem gan dung.")
