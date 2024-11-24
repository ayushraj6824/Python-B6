import numpy as np

arr = np.random.randint(1, 51, size=(2, 3))
print("Original Array:\n", arr)

mean_value = np.mean(arr)
print("Mean:", mean_value)

transpose = arr.T
print("Transpose:\n", transpose)