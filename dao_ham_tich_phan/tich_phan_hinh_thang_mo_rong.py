import math
def f(x):
    return  math.log(2.7*x+5.6, math.e)
a = 0
b = 1
n = 3
def hinh_thang_mo_rong(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        if i == 0:
            continue
        if i == n:
            break
        result += 2*f(a + i * h)
    result += (f(a) + f(b))
    
    result *= (h/2)
    return result
print("Hinh thang mo rong: ", end="")
print(hinh_thang_mo_rong(f, a, b, n))
