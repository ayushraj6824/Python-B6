import numpy as np
#broadcasting scalar
arr = np.array([1, 2, 3])
print("Array + 10:", arr + 10)
#broadcasting array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

print("Broadcasted Addition:\n", a + b)