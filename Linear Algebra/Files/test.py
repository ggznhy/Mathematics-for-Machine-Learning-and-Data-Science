import numpy as np

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.dtype(float))

b = np.array([1, 1, 1], dtype=np.dtype(float))

print(A)
print(b)

x = np.linalg.solve(A, b)
print(x)

d = np.linalg.det(A)
print(d)