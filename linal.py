import numpy as np

a=np.random.randn(3,3)
print(a)
print(a.T)
b=np.random.randn(3,3)
print(a@b)
j = np.linalg.matrix_rank(a)
print(j)