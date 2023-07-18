import math
def f(x):
    return x**3 -x -1

# Tìm nghiệm của phương trình f(x) = 0
x_initial = 1
#f(x) = 0 -> g(x) = x
def g(x):
    return math.pow(x+1, 1/3)

def fixed_point_iteration(x0, tolerance=1e-6, max_iterations=6):
    x = x0
    for i in range(max_iterations):
        x_next = g(x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    return x
    return None

solution = fixed_point_iteration(x_initial)
if solution is not None:
    print("Nghiem phuong trinh la:", solution)
else:
    print("Khong tim thay nghiem trong so lan lap cho truoc.")

# Tìm điểm bất động của hàm g(x)
fixed_point = fixed_point_iteration(x_initial, tolerance=1e-6, max_iterations=1000)
if fixed_point is not None:
    print("Diem bat dong la:", fixed_point)
else:
    print("Khong tim thay diem bat dong trong so lan lap cho truoc.")
