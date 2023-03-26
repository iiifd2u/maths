# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()

# n=int(input())
# m=int(input())
# matrix =[[input() for _ in range(m)] for _ in range(n)]
# for r in range(n):
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()
# print()
# for c in range(m):
#     for r in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# n=int(input())
# matrix =[input().split()  for _ in range(n)]
# sum =0
# for i in range(n):
#     sum+=int(matrix[i][i])
# print(sum)

# import statistics
# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
# for i in range(n):
#     print(len(list(filter(lambda x:x>statistics.mean(matrix[i]), matrix[i]))))

# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
# max=matrix[n-1][0]
# for i in range(n):
#     for j in range(n):
#         if i>=j and matrix[i][j]>max:
#             max = matrix[i][j]
# print(max)

# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
# max=matrix[n-1][0]
# for i in range(n):
#     for j in range(n):
#         if ((i>=j and i<=n-j-1) or (i<=j and i>=n-j-1)) and matrix[i][j]>max:
#             max = matrix[i][j]
# print(max)

# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
#
# di ={'Верхняя четверть':0, 'Правая четверть':0, 'Нижняя четверть':0, 'Левая четверть':0}
#
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             if i<n-j-1:
#                 di['Верхняя четверть']+=matrix[i][j]
#             elif i>n-j-1:
#                 di['Правая четверть'] += matrix[i][j]
#         elif i>j:
#             if i<n-j-1:
#                 di['Левая четверть']+=matrix[i][j]
#             elif i>n-j-1:
#                 di['Нижняя четверть'] += matrix[i][j]
# for k, v in di.items():
#     print(f'{k}: {v}')

# n=int(input())
# m=int(input())
# mult =[[[] for _ in range(m)] for _ in range(n) ]
# for r in range(n):
#     for c in range(m):
#         mult[r][c]=str(r*c)
#         print(mult[r][c].ljust(3), end='')
#     print()

# n=int(input())
# m= int(input())
# matr =[list(map(int, input().split()))  for _ in range(n)]
#
# def search(matrix):
#     mx = max([max(matrix[i]) for i in range(n)])
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] ==mx:
#                 return (f'{i} {j}')
# print(search(matr))

# n=int(input())
# m= int(input())
# matrix =[input().split()  for _ in range(n)]
# change = list(map(int, input().split()))
# matrix[change[0]], matrix[change[1]] = matrix[change[1]], matrix[change[0]]
# for i in range(n):
#     matrix[i][change[0]], matrix[i][change[1]] = matrix[i][change[1]], matrix[i][change[0]]
#     print(' '.join(matrix[i]), end='')
#     print()

# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
# ans ='YES'
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             ans = 'NO'
# print(ans)
import math
# n=int(input())
# matrix =[input().split()  for _ in range(n)]
# for c in range(n):
#     for r in range(n):
#         if c ==r:
#             matrix[r][c], matrix[n-r-1][c] =matrix[n-r-1][c], matrix[r][c]
# for i in range(n):
#     print(' '.join(matrix[i]), end='')
#     print()

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix.reverse()
# for row in matrix:
#     print(*row)

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matr = list(map(list, matrix))
# for i in range(n):
#     for j in range(n):
#         matr[j][n-i-1]=matrix[i][j]
# for row in matr:
#     print(*row)

# n= list(input())
# table = [['.' for _ in range(8)] for _ in range(8)]
# di = {'a':0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f': 5, 'g':6, 'h':7}
# row = 8-int(n[1])
# col = di[n[0]]
# table[row][col]='N'
# for i in range(8):
#     for j in range(8):
#         pos = (row-i)*(col-j)
#         if pos ==2 or pos ==-2:
#             table[i][j] = '*'
# for rw in table:
#     print(*rw)

# n=int(input())
# matrix =[list(map(int, input().split()))  for _ in range(n)]
# sm = sum(matrix[0])
# ans ='YES'
# st = set()
# for r in range(n):
#     for c in range(n):
#         if matrix[r][c]<=0:
#             ans = 'NO'
#         st.add(matrix[r][c])
#
# if len(st)!=n**2:
#     ans = 'NO'
# for r in range(1,n):
#     if sum(matrix[r]) !=sm:
#         ans = 'NO'
# for c in range(n):
#     if sum([row[c] for row in matrix])!=sm:
#         ans = 'NO'
# if sum([matrix[j][j] for j in range(n)])!=sm:
#     ans = 'NO'
# if sum([matrix[j][n-j-1] for j in range(n)]) != sm:
#         ans = 'NO'
# print(ans)

# size =list(map(int, input().split()))
# matrix = [["*" for _ in range(size[1])] for _ in range(size[0])]
#
# for i in range(size[0]):
#     for j in range(size[1]):
#         if (i+j)%2 ==0:
#             matrix[i][j] ='.'
# for row in matrix:
#     print(*row)

# n= int(input())
# matrix = [[1 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if  i<n-1-j:
#             matrix[i][j]=0
#         elif i>n-1-j:
#             matrix[i][j]=2
# for row in matrix:
#     print(*row)

# size =list(map(int, input().split()))
# matrix = [[str(i+j*size[1]+1).ljust(3) for i in range(size[1])] for j in range(size[0])]
#
# for row in matrix:
#     print(*row)
# size =list(map(int, input().split()))
# matrix = [[(str(i+(size[0]-1)*i+1+j)).ljust(3) for i in range(size[1])] for j in range(size[0])]
#
# for row in matrix:
#     print(*row)

# n= int(input())
# matrix = [['0'.ljust(3) for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i ==j or i==n-j-1:
#             matrix[i][j] = '1'.ljust(3)
#         print(matrix[i][j], end='')
#     print()

# n= int(input())
# matrix = [['0'.ljust(3) for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i <=j and i<=n-j-1) or (i >=j and i>=n-j-1):
#             matrix[i][j] = '1'.ljust(3)
#         print(matrix[i][j], end='')
#     print()

# size =list(map(int, input().split()))
# matrix = [[str((i+j)%(size[1])+1).ljust(3) for i in range(size[1])] for j in range(size[0])]
# for row in matrix:
#     print(*row)

# size =list(map(int, input().split()))
# li = [i for i in range(1, size[0]*size[1]+1)]
# matrix=[]
# for r in range(size[0]):
#     if r%2==0:
#         matrix.append(list(map(lambda x: str(x).ljust(3), li[r*size[1]:r*size[1]+size[1]])))
#     else:
#         matrix.append(list(map(lambda x: str(x).ljust(3), li[r*size[1] + size[1]-1:r*size[1]-1:-1])))
# for row in matrix:
#     print(*row)

# size =list(map(int, input().split()))
# li = [i for i in range(size[0]*size[1], 0, -1)]
# matrix = [[] for _ in range(size[0])]
# for k in range(size[0]+size[1]-1):
#     for r in range(size[0]):
#         for c in range(size[1]):
#             if k == r+c:
#                 matrix[r].append(str(li.pop()).ljust(3))
# for row in matrix:
#     print(*row)

# size =list(map(int, input().split()))
# matrix = [['0'.ljust(3) for _ in range(size[1])] for _ in range(size[0])]
# li = [i for i in range(size[0]*size[1], 0, -1)]
# kr= min(size[0],size[1])//2
# c, r=0, 0
# if kr>0:
#     for k in range(1, kr+1):
#              while c < size[1] - k:
#                  matrix[r][c] = str(li.pop()).ljust(3)
#                  c+=1
#              while r < size[0] - k:
#                  matrix[r][c] = str(li.pop()).ljust(3)
#                  r+=1
#              while c>=k:
#                  matrix[r][c] = str(li.pop()).ljust(3)
#                  c-=1
#
#              while r>=k:
#                  matrix[r][c] = str(li.pop()).ljust(3)
#                  r-=1
#              c, r =k, k
# for i in range(kr, size[0]-kr):
#     for j in range(kr, size[1] - kr):
#         matrix[i][j] = str(li.pop()).ljust(3)
# for row in matrix:
#      print(*row)

# size =list(map(int, input().split()))
# matrix1=[list(map(int, input().split(' '))) for _ in range(size[0])]
# input()
# matrix2=[list(map(int, input().split(' '))) for _ in range(size[0])]
# matrix3=[[0 for _ in range(size[1])]  for _ in range(size[0])]
# for i in range(size[0]):
#     for j in range(size[1]):
#         matrix3[i][j] = matrix1[i][j]+matrix2[i][j]
#
# for row in matrix3:
#      print(*row)

# n, m = [int(i) for i in input().split()]
# matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# _, k = [int(i) for i in input().split()]
# matrix2 = [[int(i) for i in input().split()] for _ in range(m)]
# matrix3 = [[0]*k for _ in range(n)]
# for i in range(n):
#     for j in range(k):
#         matrix3[i][j] =sum([matrix1[i][x]*matrix2[x][j] for x in range(m)])
#
# for row in matrix3:
#      print(*row)

# n = int(input())
# matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
# k= int(input())
# def multiple(matr, st):
#     if st ==2:
#         return [[sum([matrix1[i][x]*matrix1[x][j] for x in range(n)]) for i in range(n)] for j in range(n)]
#     matr= multiple(matr, st-1)
#     return [[sum([matrix1[i][x]*matr[x][j] for x in range(n)]) for i in range(n)] for j in range(n)]
# matrix2 = multiple(matrix1, k)
# for row in matrix2:
#     print(*row)