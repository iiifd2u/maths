
def iosif_flaviy(n, k):
    l = [i for i in range(1,n+1)]
    j=0
    k=k-1
    while len(l)>1:
        j+=k
        if j>=n:
            j=j%n
        l.pop(j)
        n=len(l)
        # print(l)
    return l[0]
# print(iosif_flaviy(n_i, k_i))

def iosif_rec(n, k):
    if n==1:
        return 1
    return (iosif_rec(n-1, k)+k-1)%n+1
print(f'new: {iosif_rec(7,5)}')

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
k=10
n=10
print(' k=', end='')
for i in range(1, 10):
    print( i, ' ', end='')
print()
for i in range(1, n):
    print(i, '|', end='')
    for j in range(1, k):
        print(f'{iosif_flaviy(i, j)}  ', end='')
    print()




# y=[iosif_flaviy(i, k) for i in range(k, n)]
# ax.scatter(range(k, n), y, s=2, c='red')
# plt.show()