import numpy as np

#Thay doi ham nay
def f(y,t):
    return y - t**2 + 1
y0 = 0.5 #y(0)
t0 = 0 #t0
h = 0.25 
n = 2
#Khong sua doan nay
def reverse_euler(y0, t0, h, n):
    y = np.zeros(n + 1)
    t = np.zeros(n + 1)
    y[0] = y0
    t[0] = t0
    for i in range(n):
        t[i + 1] = t[i] + h
        y[i + 1] = y[i] + h * f(y[i + 1], t[i + 1])
    return y, t
result = reverse_euler(y0 = y0, t0 = t0, h = h, n = n)
print('t: ', end='')
print(result[1])
print('y: ', end='')
print(result[0])



