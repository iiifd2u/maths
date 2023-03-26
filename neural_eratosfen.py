import numpy as np
def eratosfen(n):
    simples_set =set(range(2, n+1))
    simples =[]
    while simples_set:
        p=min(simples_set)
        simples_set-=set([el for el in range(p**2, n+1, p)])
        simples_set.remove(p)
        simples.append(p)
    return simples


print(eratosfen(200))

