'''
    Найдите оптимальные коэффициенты для построения линейной регрессии.
'''
import numpy as np
from urllib.request import urlopen

# загрузим данные из URL из входа
f = urlopen(input())
A = np.loadtxt(f, skiprows=1, delimiter=',')

# Конструируем матрицы X и Y
Y= A[:,0]
Y.shape = (Y.shape[0],1)
X = np.hstack((np.ones_like(Y), A[:,1:]))

# Считаем коэффициенты линейной регрессии
# b = (X.T * X) ** -1 * X.T * Y
#
b = np.linalg.inv(X.T @ X) @ X.T @ Y

print(*list(map('{0:.4f}'.format, b.flatten())))