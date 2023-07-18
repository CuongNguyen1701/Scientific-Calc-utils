def f(X):
    return X**2 - 2*X - 2
a = 0
b = 4
h = (b-a)/3
def simpson3_8(f, a, b, h):
    return 3*h/8 * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))
print("simpson 3/8: ", end="")
print(simpson3_8(f, a, b, h))
