import math
# Định nghĩa hàm f(x) = e^x - 2
def f(x):
    return  x*x*x + x -1

# Khoảng phân li nghiệm
a = 0
b = 1

# Độ chính xác epsilon
epsilon = 0.15

def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Không có nghiệm trong khoảng đã cho!")
        return None

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return [c, (a + b) / 2]


# Gọi hàm bisection_method để tìm nghiệm
[nghiem_ao, nghiem] = bisection_method(f, a, b, epsilon)

if nghiem is not None:
    print("Nghiem phuong trinh la:", nghiem)
    print("Sai so, lay khoang cach cua hai ket qua sau:" + str(f(nghiem_ao)) + " và " + str(f(nghiem)))

else:
    print("Khong tim thay nghiem trong khoang")  
