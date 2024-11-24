import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

print("Original 2D Array:\n", a)
print("1D Array:", b)

result = a + b  # Broadcasting
print("Broadcasted Addition:\n", result)