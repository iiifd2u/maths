import time
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
from sympy import *


# функция ошибок, ее надо минимизировать
def E(y, a, b):
    ff = np.array([a*z+b for z in range(N)])
    return np.dot((y-ff).T, (y-ff))
# частная производная по а
def dEda(y, a, b):
    ff = np.array([a * z + b for z in range(N)])
    return -2*np.dot((y-ff).T, range(N))
# частная производная по б
def dEdb(y, a, b):
    ff = np.array([a * z + b for z in range(N)])
    return -2*(y-ff).sum()

N=100
Niter = 50
sigma =3
at=0.5
bt=2

aa=0
bb=0
lmd1 =0.00001
lmd2 = 0.005

f=np.array([at*z+bt for z in range(N)])
y=np.array(f+np.random.normal(0, sigma, N))
# ax.plot(range(N), f)
# ax.scatter(range(N), y, c='red')
# plt.show()
# print(f)
# x, y, a, b, c = symbols('x y a b c')
# y = a*x*x +b*x+c
# print(diff(y, x))


for n in range(Niter):
    aa =aa-lmd1*dEda(y, aa, bb)
    bb = bb - lmd2 * dEdb(y, aa, bb)
    print(aa, bb)
ff = np.array([aa * z + bb for z in range(N)])
ax.scatter(range(N), y, s=2, c='red')
ax.plot(f)
ax.plot(ff, c='red')
ax.grid(True)
plt.show()