import numpy as np
from urllib.request import urlopen

f = urlopen(input())

A = np.loadtxt(f, skiprows=1, delimiter=',')
print(A.mean(axis=0))