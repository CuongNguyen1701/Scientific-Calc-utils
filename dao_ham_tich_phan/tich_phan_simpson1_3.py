import math

# input


def f(X):
    return math.exp(math.sin(X)) + X**2


a = 0
b = 2
h = (b - a) / 2

# code


def simpson1_3(f, a, b, h):
    return h/3 * (f(a) + 4*f((a+b)/2) + f(b))


print("simpson 1/3: ", end="")
print(simpson1_3(f, a, b, h))


def simpson1_3_mo_rong(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        if i == 0:
            continue
        if i == n:
            break
        if (i % 2 == 0):
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    result += (f(a) + f(b))

    result *= ((b - a) / (3*n))
    return result


print("simpson 1/3 mo rong: ", end="")
print(simpson1_3_mo_rong(f, a=0, b=2, n=20))
