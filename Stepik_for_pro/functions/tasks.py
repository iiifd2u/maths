# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(fancy(char2='$', length=3))

# def matrix(n=1, m=None, c=0):
#     if m==None:
#         m=n
#     return [[c for _ in range(m)] for _ in range(n)]
# print(matrix(3, 4,9))


# def f(n=3):
#     return n + 7
#
#
# print(f(f(f())))

# def count_args(*args):
#     return len(args)
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# def sq_sum(*args):
#     return sum(el**2 for el in args)
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def mean(*args):
#     a = [el for el in args if type(el) in (int, float)]
#     return sum(a)/len(a) if len(a)>0 else 0.0
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def greet(name, *args):
#     return 'Hello, ' + name + ''.join([' and '+ el for el in args ]) +'!'
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

# def print_products(*args):
#     a = [el for el in args if type(el) is str and el!='']
#     print(*[f'{i}) {el}'for i, el in zip(range(1, len(a)+1), a)], sep='\n') if len(a)!=0 else print('Нет продуктов')
#
#     # print(*[f'{i}) {el}'for i, el in zip(range(len(args)), args) if type(el) is str], sep='\n')
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

# def info_kwargs(**kwargs):
#     print(*[f'{el}: {kwargs[el]}' for el in sorted(kwargs)], sep='\n')
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39),
#            (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99),
#            (89, 9, 34), (10, 20, 30, -2), (50, 40, 50),
#            (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6),
#            (-9, 8, 4), (90, 1, -45, -21)]
# import numpy as np
# print(min(numbers, key=np.mean), max(numbers, key=np.mean), sep='\n')

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def dist(tpl):
#     return sum([el**2 for el in tpl])
# print(sorted(points, key=dist))


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39),
#            (1, 2, 3), (12, 45, 67), (-2, -4, 100),
#            (1, 2, 99), (89, 90, 34), (10, 20, 30),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def sum_mm(tpl):
#     return min(tpl)+max(tpl)
#
# print(sorted(numbers, key=sum_mm))

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
#             ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# f = int(input())
# print(*[' '.join([str(i) for i in el]) for el in sorted(athletes, key=lambda x:x[f-1])], sep='\n')

# import math
# d={'квадрат': lambda x:x**2,'куб': lambda x:x**3, 'корень': lambda x:x**0.5, 'модуль': lambda x:abs(x), 'синус': lambda x:math.sin(x) }
# n=int(input())
# print(d[input()](n))

# print(*sorted(input().split(' '), key=lambda x:sum([int(el) for el in x])))

# def sorting(el):
#     return sum([int(x) for x in el]), int(el)
#
# print(*sorted(input().split(), key=lambda x: (sum([int(el) for el in x]), int(x))))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# print(var1)
# var2 = min(map(abs, numbers))
# print(var2)
#
# print(var1 + var2)

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# print(*map(lambda x:round(x,2), numbers), sep='\n')

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434,
#            696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657,
#            1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309,
#            1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345,
#            394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898,
#            669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496,
#            370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008,
#            231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

# def func(x):
#     return True if x%5==2 and x>99 and x<1000 else False
#
# print(*map(lambda x:x**3, filter(func, numbers)), sep='\n')

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2,
#            75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90,
#            56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96,
#            58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51,
#            58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82,
#            87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64,
#            38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64,
#            94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# def sum_sq(x, y):
#     return x+y**2
# print(reduce(sum_sq, numbers, 0))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276,
#            61, 298, 280, 214, 156, 227, 228, 51, -4, 202,
#            58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49,
#            183, 166, 205, 183, 266, 180, 6, 279, 200, 208,
#            231, 178, 201, 260, -35, 152, 115, 79, 284, 181,
#            92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128,
#            143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8,
#            111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71,
#            135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211,
#            5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129,
#            274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79,
#            -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279,
#            129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10,
#            250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

# def func(x):
#     return True if len(str(abs(x)))==2 and x%7 ==0 else False
#
# print(sum(map(lambda x:x**2, filter(func, numbers))))

# def func_apply(func, li):
#     result =[]
#     for item in li:
#         new_item = func(item)
#         result.append(new_item)
#     return result
#
# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# from operator import add
# from functools import reduce
#
# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)

# high_ord_func = lambda x, func: x + func(x)
#
# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)
#
# print(result)

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2,1), floats))
# filter_result = list(filter(lambda name:len(name)>4 and name==name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

from functools import reduce
import operator
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# print('Cities:',', '.join(list(map(lambda x:x[0],sorted(filter(lambda x:x[1]>10000000 and x[2]=='primary', data), key=lambda x:x[0])))))
# l='aaaa'
# print(l.title())

# func = lambda x: x%19==0 or x%13==0
# print(func(14))

# func = lambda a:a.lower()[0]+a.lower()[-1]=='aa'
# print(func('assA'))

# import re
# is_non_negative_num = lambda x:True if ''.join(re.findall(r"\d+.\d+|\d+", x))==x and float(x) >=0 else False
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# import re
# is_num = lambda x:True if re.search(r"\-?[\d]*\.?[\d]+", x) and re.search(r"\-?[\d]*\.?[\d]+", x).group()==x else False
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('1-1'))
# print(is_num('0'))

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse',
#          'abolish', 'abuse', 'abuse', 'bid', 'wednesday',
#          'able', 'betray', 'accident', 'abduct', 'bigot',
#          'bet', 'abandon', 'besides', 'access', 'friday',
#          'bestow', 'abound', 'absent', 'beware', 'abundant',
#          'abnormal', 'aboard', 'about', 'accelerate', 'abort',
#          'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent',
#          'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# print(*sorted(filter(lambda x:len(x)==6, words)))

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80,
#            27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80,
#            80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19,
#            8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
#            57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95,
#            90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
#            37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# print(*list(map(lambda x:x//2 if x%2==0 else x, filter(lambda x:x<=47 if x%2==1 else x, numbers))))

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'),
#         (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'),
#         (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# for el in sorted(data, key=lambda x:x[1][-1], reverse=True):
#     print(f'{el[1]}: {el[0]}')

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа',
#         'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна',
#         'мир', 'случай',         'голова', 'ребенок', 'сила', 'конец', 'вид', 'система',
#         'часть', 'город', 'отношение', 'женщина', 'деньги']
# print(*sorted(sorted(data), key=lambda x:len(x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb',
#               1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970,
#               1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908,
#               'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290,
#               1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot',
#               'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard',
#               'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113,
#               1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant',
#               2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday',
#               810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid',
#               1805326, 1499197, 2241159, 605320, 2347441]
#
# print(max(mixed_list, key=lambda x: x if isinstance(x, int) else 0))
#
# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate',
#               'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday',
#               'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40,
#               26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent',
#               'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond',
#               19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89,
#               'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# print(*sorted(mixed_list, key=lambda x:(isinstance(x, str), x)))

# print(*list(map(lambda x:255-x, [int(el) for el in input().split()])))

# from functools import reduce
# from operator import add
# def evaluate(coefficients, x):
#     return reduce(add, list(map(lambda y, i:x**i*y, coefficients[::-1], range(len(coefficients)))))
# print(evaluate([int(el) for el in input().split()], int(input())))

#________________ТРАНСПОНИРОВАНИЕ МАТРИЦЫ ПРИКОЛЬНЫЙ СПОСОБ_____________________
# import random
#
# n=int(input())
# m=int(input())
#
# matrix =[[random.randint(0,100) for _ in range(m)] for _ in range(n)]
#
# for row in matrix:
#     print(*[str(el).ljust(3) for el in row])
# print()
#
# t_matrix = list(zip(*matrix))
#
# for row in t_matrix:
#     print(*[str(el).ljust(3) for el in row])
#_____________________________________________________________________________


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x:x in command, ignore))
#
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for ca, co, po in zip(capitals, countries, population):
#     print(f'{ca} is the capital of {co}, population equal {po} people.')

# abscissas=[float(el) for el in input().split()]
# ordinates=[float(el) for el in input().split()]
# applicates=[float(el) for el in input().split()]
# print(all(map(lambda x:True if x[0]**2+x[1]**2+x[2]**2<=4 else False, zip(abscissas, ordinates, applicates))))

# IP = input().split('.')
# print(all(map(lambda x: True if x.isdigit() and int(x)<=256 and int(x)>=0 else False, IP)))

# a=int(input())
# b=int(input())
#
# print(*[el for el in range(a, b+1) if all(x!='0' and el%int(x)==0 for x in str(el))])

# pas = input()
# print('YES' if all([any([1 for el in pas if el.islower()]),any([1 for el in pas if el.istitle()]), any([1 for el in pas if str(el).isdigit()]), len(pas)>=7]) else 'NO')

n=int(input())
good_boys =[]
for i in range(n):
    k=int(input())
    cl = [input().split()[1] for x in range(k)]
    good_boys.append(any(map(lambda x:1 if x=='5' else 0, cl)))
print(['NO', 'YES'][all(good_boys)])

