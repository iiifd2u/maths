import random

# n = int(input())    # количество попыток
# [print(["Орел", "Решка"][random.randint(0, 1)]) for _ in range(n)]

# n = int(input())
# [print(random.randint(1, 6)) for _ in range(n)]

# n=int(input())
# a=[[chr(random.randint(65, 90)).lower(), chr(random.randint(65, 90)).upper()][random.randint(0, 1)] for _ in range(n)]
# print(''.join(a))

# s =set()
# while len(s)<7:
#     s.add(random.randint(1, 49))
# print(*sorted(s))

# def generate_ip():
#     return  f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 9)}.{random.randint(0, 255)}'

# from string import ascii_uppercase as ul
# def generate_index():
#     return f'{random.choice(ul)}{random.choice(ul)}{random.randrange(100)}_{random.randrange(100)}{random.choice(ul)}{random.choice(ul)}'
# print(generate_index())

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# random.shuffle(matrix)
# for row in matrix:
#     print(*row)

# s=set()
# while len(s)<100:
#     s.add(''.join([str(random.randrange(1,10))] +[str(random.randrange(10)) for _ in range(6)]))
# print(*s, sep='\n')

# word =list(input())
# random.shuffle(word)
# print(''.join(word))

# s=set()
# while len(s)<25:
#     s.add(str(random.randint(1, 75)).ljust(3))
# matrix=[list(s)[j*5:j*5+5] for j in range(5)]
# matrix[2][2]='0'.ljust(3)
# for row in matrix:
#     print(*row)

# n= int(input())
# li =[input() for _ in range(n)]
# random.shuffle(li)
# for i in range(n):
#     print(f'{li[(i+1)%n]} - {li[(i+2)%n]}')

# from string import ascii_letters as letters
# from string import digits as digs
# symbs = list(set(letters+digs)-set('oO0Il1'))
# def generate_password(length):
#     return ''.join(random.sample(symbs, length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

# from string import ascii_uppercase as ul
# from string import ascii_lowercase as ll
# from string import digits as digs
# ul = list(set(ul)-set('IO'))
# ll = list(set(ll)-set('lo'))
# digs=list(set(digs)-set('10'))
# keys= set()
# n, m = int(input()), int(input())
#
#
# def generate_password(length):
#     for i in range(1, length - 1):
#         for j in range(1, length - 1):
#             for k in range(1, length - 1):
#                 if i + j + k == length and k<len(digs):
#                     keys.add((i, j, k))
#     i, j, k = random.choice(list(keys))
#     a=random.sample(ul, i)+random.sample(ll, j)+random.sample(digs, k)
#     random.shuffle(a)
#     return ''.join(a)
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# print(*generate_passwords(n, m), sep='\n')

# import random
#
# n = 10**6
# k=0
# for i in range(n):
#     x =random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#     if x**3+y**4+2>=0 and 3*x+y**2<=2:
#         k+=1
# print(k/n*16)

# import random
#
# n = 10**6
# k=0
# for i in range(n):
#     x =random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x**2+y**2<=1:
#         k+=1
# print(k/n*4)

