from scipy.interpolate import lagrange
x = [-1, 1, 2]
y = [1, 2, 3]
result = lagrange(x, y)
print("ham noi suy lagrange: ")
print(result)