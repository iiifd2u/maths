# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
# print(min(my_dict)+max(my_dict))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# print(*sorted([users[i]['name'] for i in range(len(users)) if users[i]['phone'][-1]=='8']))
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# res1=list(x['name'] for x in list(filter(lambda x:'email' not in x, users)))
# res2 = list(x['name'] for x in list(filter(lambda x:'email' in x, users)) if x['email']=='')
# print(*sorted(res1+res2))

# d={
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# print(*[d[k] for k in list(input())])

# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# key = input()
# print(f'{key}: {d[key]}')

# d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
#
# print(''.join([d[el] for el in list(input().upper().replace('"', '')) ]))

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
#          '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
#          '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# d =dict(zip(letters, morse))
# print(*[d[k] for k in list(input().upper()) if k in letters])

# result = {}
# for k in range(1,16):
#     result[k]=k**2
#
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result =dict1.copy()
# for k in dict2.keys():
#     if k in dict1:
#         result[k]=dict1[k]+dict2[k]
#     else:
#         result[k]=dict2[k]
# print(result)

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# st=set(text)
# for s in st:
#     result[s]=text.count(s)
# print(result)
# result = {}
# for c in text:
#     result[c] = result.get(c, 0) + 1

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana ' \
#     'orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
#     'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate' \
#     ' barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot ' \
#     'currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange ' \
#     'melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result={}
# max_len=0
# for el in s.split():
#     result[el]=result.get(el, 0)+1
#     max_len = result[el] if max_len<result[el] else max_len
# print(sorted(list(filter(lambda el:el[1]==max_len, sorted(result.items(), key=lambda x:x[1], reverse=True))), key=lambda x:x[0])[0][0])

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}
# for el in pets:
#     result[tuple(el[1:])]=result.setdefault(tuple(el[1:]), '')+el[0]+' '
# for k in result:
#     result[k] = result[k].split()
# print(result)
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])

# str = input().lower().split()
# result={}
# for el in str:
#     result[el.strip('.,!?:;-')] = result.get(el.strip('.,!?:;-'), 0)+1
# print(min(el for el in result if result[el]==min(result.values())))

# str=input().split()
# result ={}
# a=[]
# for el in str:
#     result[el]=result.get(el, 0)+1
#     if result[el]>1:
#        a.append(el+f'_{result[el]-1}')
#     else:
#         a.append(el)
# print(*a)

# n = int(input())
# li_dict =[input().split(': ') for _ in range(n)]
# m = int(input())
# li_req =[input() for _ in range(m)]
# dict ={}
# for i in range(n):
#     dict[li_dict[i][0].lower()]=li_dict[i][1]
# for el in li_req:
#     print(dict.get(el.lower(), 'Не найдено'))



# li = list((input()+input()).lower())
# dict={}
# anw ='YES'
# for el in li:
#         dict[el]= dict.get(el, 0)+1
# for v in dict.values():
#     if v%2!=0:
#         anw='NO'
# print(anw)


# dict={}
# for k in range(-1, 2, 2):
#     for el in input().lower().split():
#         for v in el.strip(' .,!?:;-'):
#             dict[v]= dict.get(v, 0)-k
# print('YES') if set(dict.values())=={0} else print('NO')

# n=int(input())
# dict={}
# for el in range(n):
#     a=input().split()
#     dict[a[0]]=a[1]
# word =input()
# for k, v in dict.items():
#     if k ==word:
#         print(v)
#     if v==word:
#         print(k)

# n=int(input())
# dict={}
# for i in range(n):
#     a = input().split()
#     dict[a[0]]=a[1:]
# m=int(input())
# for i in range(m):
#     str = input()
#     for k, v in dict.items():
#         if str in v:
#             print(k)

# n=int(input())
# a=[[el.lower() for el in input().split()] for _ in range(n)]
# dict={}
# for el in a:
#     dict[el[1]]=[el[0]] if not dict.get(el[1], 0) else dict[el[1]]+[el[0]]
# m=int(input())
# print(*[' '.join(dict.get(input().lower(), ['абонент', "не", "найден"])) for _ in range(m)], sep='\n')

# word=list(input())
# dict_word = {}
# for el in word:
#     dict_word[el] = dict_word.get(el, 0)+1
# n=int(input())
# code = dict(map(lambda x:[int(x[1]), x[0]], [input().split(': ') for _ in range(n)]))
# [print(code[dict_word[v]], end='') for v in word]

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i:numbers[i]**2 for i in range(len(numbers))}
# print(result)

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {k:colors[k] for k in colors.keys() if colors[k]!=None}
# result ={k:v for k, v in colors.items() if v}
# print(result)

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {k:v for k, v in favorite_numbers.items() if len(str(v))==2}
# print(result)

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {v:k for k, v in months.items()}
# print(result)

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(el.split(':')[0]):el.split(':')[1] for el in s.split()}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {el:[i for i in range(1, int(el)+1) if el%i==0] for el in numbers}
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result={el:[ord(v) for v in el] for el in words}
# print(result)

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k:v for k, v in letters.items() if k not in remove_keys}
# print(result)

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k:v for k, v in students.items() if (v[0]>167 and v[1]<75)}
# print(result)

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {el[0]:(el[1], el[2]) for el in tuples}
# print(result)

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{st_i:{st_n:st_g}} for st_i, st_n, st_g in zip(student_ids, student_names, student_grades)]
# print(result)
