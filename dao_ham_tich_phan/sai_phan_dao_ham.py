import numpy as np
import math
def f(x):
    return math.log(2.7*x+5.6, math.e)

h = 0.0001  # Độ dịch chuyển nhỏ
x0 = 1
def f_sai_phan_thuan(f, x):
    return (f(x + h) - f(x)) / h
def f_sai_phan_nguoc(f, x):
    return (f(x) - f(x - h)) / h
def f_sai_phan_trung_tam(f, x):
    return (f(x + h) - f(x - h)) / (2 * h)
def f_dao_ham_cap_2(f, x):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

print('f_sai_phan_thuan: ', end='')
print(f_sai_phan_thuan(f, x0))
print('f_sai_phan_nguoc: ', end='')
print(f_sai_phan_nguoc(f, x0))
print('f_sai_phan_trung_tam: ', end='')
print(f_sai_phan_trung_tam(f, x0))
print('f_dao_ham_cap_2: ', end='')
print(f_dao_ham_cap_2(f, x0))
