

# lst = [i for i in input().split()]
# n =int(input())
# new_lst = [[] for _ in range(n)]
# for i in range(len(lst)):
#     new_lst[i%n].append(lst[i])
# print(new_lst)

# n=int(input())
# matrix = [[i for i in input().split()] for _ in range(n)]
# a =[]
# for r in range(n):
#     for c in range(n):
#         if r>=n-c-1:
#             a.append(matrix[r][c])
# print(max(a))

# n=int(input())
# matrix = [[i for i in input().split()] for _ in range(n)]
# for r in range(n):
#     for c in range(n):
#         if c>r:
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
# for row in matrix:
#     print(*row)

# n=int(input())
# matrix = [['.']*n for _ in range(n)]
# for r in range(n):
#     for c in range(n):
#         if r==c or r==n-c-1 or r==n//2 or c==n//2:
#             matrix[r][c]="*"
# for row in matrix:
#     print(*row)

# n=int(input())
# matrix = [[i for i in input().split()] for _ in range(n)]
# answ ='YES'
# for r in range(n):
#     for c in range(n):
#         if matrix[r][c]!=matrix[c][n-r-1]:
#             answ='NO'
# print(answ)

# n=int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for row in matrix:
#     print(*row)
# li =[i for i in range(1, n+1)]
# answ ='YES'
# for r in matrix:
#     if sum(r)!=sum(li):
#         answ='NO'
# for r in range(n):
#     count =0
#     lst = [i for i in range(1, n + 1)]
#     for c in range(n):
#         count+= matrix[r][c]
#         if matrix[r][c] not in lst:
#             answ = 'NO'
#         else:
#             lst.pop(lst.index(matrix[r][c]))
#             print(f'{matrix[r][c]}-r={r}-c={c}')
#             print(lst)
#     if count!=sum(li):
#         answ = 'NO'
# print(answ)

# n=int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# li =[i for i in range(1, n+1)]
# answ ='YES'
# for r in matrix:
#     r_i=r.copy()
#     r_i.sort()
#     if r_i!=li:
#         answ='NO'
#
# for c in range(n):
#     c_i=[]
#     for r in range(n):
#         c_i.append(matrix[r][c])
#     c_i.sort()
#     if c_i!=li:
#         answ='NO'
# print(answ)

# pos = list(input())
# table = [['.' for _ in range(8)] for _ in range(8)]
# di = {'a':0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f': 5, 'g':6, 'h':7}
# col=di[pos[0]]
# row=8-int(pos[1])
# for r in range(8):
#     for c in range(8):
#         if r==row or c==col or r+c==col+row or (r-row)==(c-col):
#             table[r][c]='*'
# table[row][col]="Q"
# for row in table:
#     print(*row)
# n=int(input())
# matrix=[[0 for _ in range(n)]for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         matrix[i][j]=abs(i-j)
# for row in matrix:
#     print(*row)

