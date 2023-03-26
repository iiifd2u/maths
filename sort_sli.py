import random
import numpy as np
# n, m = [int(el) for el in input().split()]
# a=[[random.randint(0, 100) for _ in range(n)] for _ in range(m)]
#
#
# for row in a:
#     print(*[str(el).ljust(3) for el in row])
#
# b=random.shuffle(a)
# print(a)

# Метод слияния двух сортированных списков

a = [1, 4, 6, 8]
b=[-3, 6]

n = len(a)
m = len(b)
i=j=0
c =[]
while i <n and j<m:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
c=c+a[i:]+b[j:]
print(c)


