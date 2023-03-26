from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import time

fig, ax = plt.subplots()
N=100
Niter=50
at=0.3
bt=2
ct=1
sigma =3

def E(y, a, b, c):
    ff = np.array([a*z**2+b*z+c for z in range(-N, N)])
    return np.sum([(y[i]-ff)**2 for i in range(-N, N)])

def dEda(y, a, b, c):
    ff = np.array([a*z**2+b*z+c for z in range(-N, N)])
    return np.sum([-2*(y-ff)*i**2 for i in range(-N, N)])

def dEdb(y, a, b, c):
    ff = np.array([a*z**2+b*z+c for z in range(-N, N)])
    return np.sum([-2*(y-ff)*i for i in range(-N, N)])

def dEdc(y, a, b, c):
    ff = np.array([a*z**2+b*z+c for z in range(-N, N)])
    return (-2*(y-ff)).sum()


f=np.array([at*z**2+bt*z+ct for z in range(-N, N)])
y=np.array(f+np.random.normal(0, sigma, 2*N))
# print(E(y, at, bt, ct))
# print(dEda(y, at, bt, ct))
# print(dEdb(y, at, bt, ct))
# print(dEdc(y, at, bt, ct))

aa=0
bb=0
cc=0
lmd1 =0.00000000000012
lmd2 = 0.00000000005
lmd3 = 0.000000001

for n in range(Niter):
    aa =aa-lmd1*dEda(y, aa, bb, cc)
    bb = bb - lmd2 * dEdb(y, aa, bb, cc)
    cc = cc - lmd3 * dEdc(y, aa, bb, cc)
    print(aa, bb, cc)

ff=np.array([aa*z**2+bb*z+cc for z in range(-N, N)])
# ax.scatter(range(N), y, s=2, c='red')
# ax.plot(f)
# ax.plot(ff, c='red')
ax.plot(range(-N, N), f)
ax.plot(range(-N, N), ff, c='green')
ax.scatter(range(-N, N), y, s=2,  c='red')
ax.grid()
plt.show()

# y=np.array(f+np.random.normal(0, sigma, N))