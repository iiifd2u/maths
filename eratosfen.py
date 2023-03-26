#Решето Эратосфена:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import *
# print('enter n:')
# n = int(input())
new_dict = {}
arrX= []
arrY=[]
for n in range(10, 1001, 99):
    for i in range(2,n+1):
        new_dict.update({i: True})
    a =[]
    def eratosfen(dct):
        p = 2
        while p**2 <=n:
            for j in range(p**2, n+1):
                if j%p==0:
                    dct[j] = False
            for idx, elem in dct.items():
                if elem and idx >p:
                    p= idx
                    break
        return dct

    eratosfen(new_dict)
    for idx, elem in new_dict.items():
        if elem:
            a.append(idx)
    arrX.append(n)
    arrY.append(len(a))

print(pd.Series(a))
fig, ax = plt.subplots()
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
# x=np.linspace(0, 20, 100)
ax.plot(arrX, arrY)
# y=x**e
# ax.plot(x,y)
plt.show()
# print(*range(1000, 0, -7))

