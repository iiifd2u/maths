# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     a =f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'
#     return a
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))
#
# print(result)

# print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))

# from functools import reduce
#
# numbers = [1, 2, 3]
# result = reduce(lambda a, b: a * b, numbers, 10)
# print(result)

# def concat(*args, sep=' '):
#     a=''
#     for el in args:
#         a+=str(el)+sep
#     return a[:-1]

# def concat(*args, sep=' '):
#     return sep.join(list(map(str, args)))
#
# print(concat('hello', 'python', 'and', 'stepik'))


# from functools import reduce
# def product_of_odds(data):   # data - список целых чисел
#     return reduce(lambda a, b: a*b, list(filter(lambda x:x%2==1, data)),1 )
#
#
# print(product_of_odds([7, 2, 3, 4]))

# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"', words))

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x)!=str(x)[::-1], numbers))

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x:sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)

# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
# def call(func, *args):
#     return func(*args)
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# def compose(f, g):
#     return lambda x: f(g(x))
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

# def arithmetic_operation(operation):
#     def func(x, y):
#         d = {'+':lambda x, y:x+y, '-':lambda x, y:x-y, '*':lambda x, y:x*y, '/':lambda x, y:x/y}
#         return d[operation]
#     return func
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))


# def arithmetic_operation(operation):
#     d = {'+':lambda x, y:x+y, '-':lambda x, y:x-y, '*':lambda x, y:x*y, '/':lambda x, y:x/y}
#     return d[operation]
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

# print(*sorted(input().split(), key=lambda x:x.lower()))


# n = int(input())
# words = [input() for _ in range(n)]
#
# def gem(word):
#     sum=0
#     for el in word.upper():
#         sum+=ord(el)-ord('A')
#     return sum
#
# print(*sorted(sorted(words), key=gem), sep='\n')

# n=int(input())
# ips = [input().split('.') for _ in range(n)]
#
# def decim(li):
#     return 256**3*int(li[0])+256**2*int(li[1])+256*int(li[2])+int(li[3])
#
# for el in sorted(ips, key=decim):
#     print('.'.join(el))

# def pretty_print(data, side='-', delimiter='|'):
#     word = delimiter +' '+f' {delimiter} '.join([str(el) for el in data])+' '+delimiter
#     print(' ' + side*(len(word)-2))
#     print(word)
#     print(' ' +side * (len(word) - 2))
#
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')