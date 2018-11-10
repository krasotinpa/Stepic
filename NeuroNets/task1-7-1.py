import numpy as np

X  = np.array([[1, 60],
                [1, 50],
                [1, 75]
])

Y = np.array([
    [10],
    [7],
    [12]
])

XtX1 = np.linalg.inv(X.T @ X)
b = XtX1 @ X.T @ Y

print(b.flatten())
print(b)
print('{0:.3f}, {1:.3f}'.format(*b.flatten()))