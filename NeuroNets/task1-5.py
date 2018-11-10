import numpy as np

A = np.eye(3, 4) * 2
B = np.eye(3, 4, 1)
mat = (A + B).flatten().reshape(12,1)

print(mat)

