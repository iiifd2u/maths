import numpy as np

a =  np.random.randint(-15, 15, (2,2), dtype='int16')
b= np.random.randint(-15, 15, (2,1), dtype='int16')

def gauss_method(A, B):
    a0 = np.c_[A, B]
    print(a0)
    for i in range(a0.shape[0]):
        for j in range(a0.shape[1]):
            print(a0[i,j])

gauss_method(a, b)

# print(b)