import numpy as np

identity_matrix = np.eye(3)
random_matrix = np.random.randint(1, 10, size=(3, 3))

print("Identity Matrix:\n", identity_matrix)
print("Random Matrix:\n", random_matrix)

result = np.dot(identity_matrix, random_matrix)
print("Result of Multiplication:\n", result)