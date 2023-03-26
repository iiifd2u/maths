# set1 = {'Yellow', 'Orange', 'Black'}
# set2 = {'Orange', 'Blue', 'Pink'}
#
# set1.difference_update(set2)

# n=int(input())
# m=int(input())
# k=int(input())
# p=int(input())
# print(n-m-k+p)

# a = [int(el) for el in input().split()]
# print(len(a)-len(set(a)))
# n= int(input())
# a=[input() for _ in range(n)]
# new =input()
# print('OK') if new not in a else print('REPEAT')

# m = int(input())
# n=int(input())
# have= [input() for _ in range(m)]
# read = [input() for _ in range(n)]
#
# for el in read:
#     print('YES') if el in have else print('NO')

# set1={int(el) for el in input().split()}
# set2={int(el) for el in input().split()}
# print(*sorted(set1&set2, reverse=True)) if set1&set2!=set() else print('BAD DAY')

# set1={int(el) for el in input().split()}
# set2={int(el) for el in input().split()}
# print('YES') if set2==set1 else print('NO')

# m= int(input())
# n= int(input())
# math= {input() for _ in range(m)}
# info = {input() for _ in range(n)}
# print(len(math-info))

# m= int(input())
# n= int(input())
# math= {input() for _ in range(m)}
# info = {input() for _ in range(n)}
# print(len(math.symmetric_difference(info))) if math.symmetric_difference(info)!=set() else print('NO')

# set1=set(input().split())
# set2=set(input().split())
# print(*sorted(set1|set2))

# m= int(input())
# n= int(input())
# all= [input() for _ in range(m+n)]
# s =set(all)
# for i in range(len(all)-1):
#     if all[i] in all[i+1:]:
#         s.remove(all[i])
# print(len(s)) if s!=set() else print('NO')

m= int(input())
a=[{input() for _ in range(int(input()))} for _ in range(m)]
s=a[0]
for el in a:
    s=s&el
print(*sorted(s), sep='\n')


