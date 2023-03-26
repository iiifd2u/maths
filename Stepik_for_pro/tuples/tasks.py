# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# last = countries[-1]
# print(last)

# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
#
# print(min(numbers)+max(numbers))

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
# print((1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13))
# print(numbers1*2+numbers2*9+numbers3)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples =list(filter(lambda x:len(x)>0, tuples))
#
# print(non_empty_tuples)
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [tuple(list(el)[:-1]+[100]) for el in tuples]
#
# print(new_tuples)
#
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# mult=1
# for el in numbers:
#     mult*=el
# print(mult)
# data = 'Python для продвинутых!'
#
# print(tuple(data))

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data=tuple(list(poet_data)[:-1]+['Москва'])
# print(poet_data)

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# print(list(map(lambda el:sum(el)/len(el), list(numbers))))

# a=int(input())
# b=int(input())
# c=int(input())
# print((-b/(2*a), (4*a*c-b**2)/(4*a)))
# n=int(input())
# li= [input().split(' ') for _ in range(n)]
# li_good=list(filter(lambda el:el[1]>'3', li))
# for el in li:
#     print(*el)
# print()
# for el in li_good:
#     print(*el)

# n= int(input())
# n1, n2, n3 =1, 1, 1
# for i in range(n):
#     print(n1, end=' ')
#     n1, n2, n3 =n2, n3, n1+n2+n3