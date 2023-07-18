import numpy as np
# input


def f(xk):
    return xk[0]**2 + xk[1]**2 + xk[2]**3 - 5*xk[3]


xk = np.array([0, 0, 0, 0])
alpha = 2
epsilon = 0.001

# code


def partial_derivative(f, xk, index, epsilon):
    xk_plus = xk
    xk_minus = xk
    xk_plus[index] += epsilon
    xk_minus[index] -= epsilon
    return (f(xk_plus) - f(xk_minus))/(2*epsilon)


def gradient(f, xk, epsilon):
    result = np.zeros(xk.shape)
    for i in range(xk.shape):
        result[i] = partial_derivative(f, xk, i,  epsilon)
    return result


while True:
    xk = xk - alpha * gradient(f, xk, epsilon)
