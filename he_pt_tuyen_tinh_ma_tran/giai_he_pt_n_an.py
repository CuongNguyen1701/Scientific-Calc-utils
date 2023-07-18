import numpy as np
from numpy.linalg import inv, LinAlgError, det

matrixA = np.array([
                    [21, 2, 3], 
                    [4, 5, 56], 
                    [7, 13, 9]
                    ])
matrixB = np.array([1, 2, 3])

try:
    determinant = det(matrixA)
    if np.isclose(determinant, 0.0):
        raise LinAlgError("Singular matrix")

    result = inv(matrixA).dot(matrixB)
    print("result:")
    print(result)

except LinAlgError as e:
    print("Error:", e)
