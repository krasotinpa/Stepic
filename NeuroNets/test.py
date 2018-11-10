import numpy as np

y_hat = np.array([[1.1], [2.1], [0.1], [3.1]])
y = np.array([[1.], [2.], [0.], [3.]])

#print(0.5 * np.mean((y_hat - y)**2))
#print(0.5 * ((y_hat - y)** 2).sum())

X = np.arange(50).reshape(10, 5)
print(X)

batch_idx = np.random.choice(X.shape[0], 5, replace=False)
print(batch_idx)
print(X[batch_idx,:])
