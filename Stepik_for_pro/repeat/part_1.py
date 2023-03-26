# import math
#
# a = int(input())
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(math.sqrt(math.pow(a, 10)+math.pow(b, 10)))

# mass = float(input())
# height = float(input())
#
# def IMT(m, h):
#     if m/(h**2)>25:
#         return 'Избыточная масса'
#     elif m/(h**2)<18.5:
#         return 'Недостаточная масса'
#     return 'Оптимальная масса'
#
# print(IMT(mass, height))

# s = input()
#
# kop = int(len(s)*60%100)
# rub = int(len(s)*60//100)
# print(f'{rub} р. {kop} коп.')

# s = input()
# print(len(input().split()))
# num=int(input())
# dict={8:'Дракон', 9:"Змея", 10:"Лошадь",
#    11:"Овца", 0:'Обезьяна', 1:"Петух",
#    2:"Собака", 3:"Свинья", 4:'Крыса',
#    5:"Бык", 6:"Тигр", 7:"Заяц"}
#
# def zodiac(n, d):
#    return d[n%12]
#
# print(zodiac(num, dict))

# n= list(input())
# if len(n)>5:
#     a=n[0]
#     n = n[-5:]
#     n.reverse()
#     n.insert(0, a)
# else:
#     n.reverse()
# if n[0]=="0":
#     n = [el for el in filter(lambda i: i!="0", n)]
# print(''.join(n))

# n=list(input())
# l = len(n)
# for i in range((l-1)//3):
#     n.insert(l-3*(i+1), ',')
# print(''.join(n))

#Задача Иосифа Флавия для к =2:
# n= int(input())
# k=int(input())
# b=''
# while n>0:
#     b=str(n%2)+b
#     n=n//2
# l=list(b)
# d = (l.pop(0))
# l.append(d)
# print(int(''.join(l), 2))

# n_i= int(input())
# k_i=int(input())

# def iosif_flaviy(n, k):
#     l = [i for i in range(1,n+1)]
#     j=0
#     k=k-1
#     while len(l)>1:
#         j+=k
#         if j>=n:
#             j=j%n
#         l.pop(j)
#         n=len(l)
#         # print(l)
#     return l[0]
# print(iosif_flaviy(n_i, k_i))
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# k=3
# n=500
# for i in range(k, n):
#     print(i, iosif_flaviy(i, k))
# y=[iosif_flaviy(i, k) for i in range(k, n)]
# ax.scatter(range(k, n), y, s=2, c='red')
# plt.show()

n_i= int(input())
k_i=int(input())
def iosif_rec(n, k):
    if n==1:
        return 1
    return (iosif_rec(n-1, k)+k-1)%n+1
print(iosif_rec(n_i, k_i))





