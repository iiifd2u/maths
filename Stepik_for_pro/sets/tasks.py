# n=int(input())
# m=int(input())
# k=int(input())
# x=int(input())
# y=int(input())
# z=int(input())
# print(n+m+k-x-y+z)

# n, m, k, x, y, z, t, a =[int(input()) for _ in range(8)]
# nm=n+m-t-x
# mk=k+m-t-y
# kn=n+k-t-z
# one =n-nm-kn-t+m-nm-mk-t+k-mk-kn-t
# two =nm+mk+kn
# print(one)
# print(two)
# print(a-one-two -t)

# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers)/len(numbers)
#
# print(average)

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum(list(map(lambda el:el**2, list(numbers)))))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# print(*sorted(fruits, reverse=True), sep='\n')

# print(len(set(input())))
# n=input()
# if len(list(n)) == len(set(n)):
#     print('YES')
# else:
#     print('NO')

# n=list(input())
# m=list(input())
# if len(set(n+m)) == 10:
#     print('YES')
# else:
#     print('NO')


# n=set(input())
# m=set(input())
# if n==m:
#     print('YES')
# else:
#     print('NO')

# li=list(input())
# if set(li[0])==set(li[1])==set(li[2]):
#     print('YES')
# else:
#     print('NO')

# n=int(input())
# sets = [set(input().lower()) for _ in range(n)]
# [print(len(el)) for el in sets]


# print(len(set(''.join([input().lower() for _ in  range(int(input()))]))))
# print(len(set([el.strip('.,;:-?!') for el in (input()).lower().split()])))

# n=[int(el) for el in input().split()]
# s =set(n)
# for el in n:
#     if el in s:
#         s.remove(el)
#         print('NO')
#     else:
#         print('YES')

# print(len(set(input().split())&set(input().split())))

# print(' '.join([str(el) for el in sorted([str(el) for el in set([int(el) for el in input().split()])&set([int(el) for el in input().split()])])]))
# print(' '.join([str(el) for el in list(sorted(set([int(el) for el in input().split()])&set([int(el) for el in input().split()])))]))
# print(*sorted(set(input().split()) & set(input().split()), key=int))
# print(*sorted(set(input().split()) - set(input().split()), key=int))

# li =[set(list(input())) for _ in range(int(input()))]
# print(*sorted(li[0].intersection(*li[1:])))

# word = 'beegeek'
# set1 = set(word*3)
# set2 = set(word[::-1]*2 + 'stepik')
# print(word[::-1]*2)
# print(set1)
# print(set2)
# print(set1 < set2)

# print('NO') if set(input()).isdisjoint(set(input())) else print('YES')

# print('NO') if set(input()).issuperset(set(input())) else print('YES')

# print(*sorted((set([int(el) for el in input().split()])&set([int(el) for el in input().split()]))-set([int(el) for el in input().split()]), reverse=True))

# set1 = set([int(el) for el in input().split()])
# set2 = set([int(el) for el in input().split()])
# set3 = set([int(el) for el in input().split()])
# res =set1&set2&set3
# print(*sorted(set1.union(set2, set3)-res))

# set1 = set([int(el) for el in input().split()])
# set2 = set([int(el) for el in input().split()])
# set3 = set([int(el) for el in input().split()])
# print(*sorted(set(range(11))-set1.union(set2, set3)))

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# print(*sorted({int(el) for el in items}))

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# print(*sorted({el.lower()[0] for el in words}))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth
# in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style
# (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended,
# with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk;
# a furry warmth, golden midges.'''

# print(*sorted({el.strip('/(/).,;:-?!') for el in sentence.lower().split()}))
# print(*sorted({el.strip('/(/).,;:-?!') for el in sentence.lower().split() if len(el.strip('/(/).,;:-?!'))<4}))

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py',
         'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt',
         'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
print(*sorted({el.lower() for el in files if set(el.lower().split('.')).issuperset({'png'})}))