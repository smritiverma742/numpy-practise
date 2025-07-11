import numpy as np

# 1) How to get the positions where elements of two arrays match?
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.where(a == b)
print(c)

# 2) How to extract all numbers between a given range from a numpy array?
a = np.array([2, 6, 1, 9, 10, 3, 27])
b = np.where((a >= 5) & (a <= 10))
print(a[b])

# 3) How to make a Python function that handles scalars to work on numpy arrays?
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

# Vectorizing the function to work with numpy arrays
pairmax = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pairmax(a, b))

# 4) How to swap two columns in a 2D numpy array?
arr = np.arange(9).reshape(3, 3)
c = arr[:, [1, 0, 2]]
print(c)

# 5) How to swap two rows in a 2D numpy array?
arr = np.arange(9).reshape(3, 3)
c = arr[[1, 0, 2], :]
print(c)

# 6) How to reverse the rows of a 2D array?
arr = np.arange(9).reshape(3, 3)
b = arr[::-1]
print(b)

# 7) How to reverse the columns of a 2D array?
arr = np.arange(9).reshape(3, 3)
b = arr[:, ::-1]
print(b)

# 8) How to create a 2D array containing random floats between 5 and 10?
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

# 9) How to print only 3 decimal places in a numpy array?
rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print(rand_arr[:4])

# 10) How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
np.random.seed(100)
rand_arr = np.random.random([3, 3]) / 1e3
np.set_printoptions(suppress=True)
print(rand_arr)
