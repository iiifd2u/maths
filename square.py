import numpy as np
n=int(input())
l=int(input())

def scuare(N, L):
    return np.round(N*L**2/(4*np.tan(np.deg2rad(180/N))), 2)

print(scuare(n, l))