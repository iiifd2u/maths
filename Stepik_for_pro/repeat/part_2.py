# n=int(input())
# l=[input() for i in range(n)]
# d = {1:0, 2:0, 3:0, 4:0}
# for el in l:
#     spl = el.split(' ')
#     print(spl)
#     a = list(map(int, spl))
#
#     if a[0]>0 and a[1]>0:
#         d[1]+=1
#     elif a[0]>0 and a[1]<0:
#         d[4]+=1
#     elif a[0]<0 and a[1]<0:
#         d[3]+=1
#     elif a[0] < 0 and a[1] > 0:
#         d[2] += 1
# print(f'Первая четверть: {d[1]}')
# print(f'Вторая четверть: {d[2]}')
# print(f'Третья четверть: {d[3]}')
# print(f'Четвертая четверть: {d[4]}')

# n= list(map(int, input().split(' ')))
# sum =0
# for i in range(1, len(n)):
#     if n[i]> n[i-1]:
#         sum+=1
# print(sum)

# n= list(map(int, input().split(' ')))
# for i in range(0, len(n)-1, 2):
#     n[i], n[i+1] = n[i+1], n[i]
# print(' '.join(list(map(str, n))))

# n= input().split(' ')
# a=n[-1]
# n.insert(0, a)
# n.pop()
# print(' '.join(n))

# n= list(map(int, input().split(' ')))
# a=[]
# for i in range(len(n)):
#     if n[i] not in a:
#         a.append(n[i])
# print(len(a))

# num = int(input())
# lst = [int(input()) for i in range(num)]
# last = int(input())
# def checker(li, ls):
#         for i in range(len(li)):
#             for j in range(len(li)):
#                 if li[i]*li[j] == ls:
#                     if i != j:
#                         return 'ДА'
#         return 'НЕТ'
# print(checker(lst, last))

# tmr = input()
# rus = input()
#
# def zuefa(fst, scd):
#     d = {1: 'камень', 2: 'ножницы', 3: 'бумага'}
#     for k, v in d.items():
#         if v == fst:
#             fst = k
#         if v ==scd:
#             scd =k
#     a = scd -fst
#     if a ==0:
#         return 'ничья'
#     elif  a==2 or a ==-1:
#         return 'Руслан'
#     else:
#         return 'Тимур'
# print(zuefa(tmr, rus))

# tmr = input()
# rus = input()
# d = {0: 'ножницы', 1: 'бумага', 2: 'камень', 3: 'ящерица', 4: 'Спок'}
# for k, v in d.items():
#      if v == tmr:
#          tmr = k
#      if v ==rus:
#          rus =k
# def check_win(fst, scd):
#     i = (fst+1)%5
#     j=(fst+3)%5
#     if fst ==scd:
#         return 'ничья'
#     elif scd == i or scd ==j:
#         return 'Тимур'
#     else:
#         return 'Руслан'
# print(check_win(tmr, rus))

# print(len(max(input().split('О'))))

# n= int(input())
# lst = [list(input()) for i in range(n)]
# def checker(st):
#         for idx1 in range(len(st)):
#             if st[idx1]=='a':
#                 st =st[idx1+1:]
#                 for idx2 in range(len(st)):
#                     if st[idx2] == 'n':
#                         st = st[idx2+1:]
#                         for idx3 in range(len(st)):
#                             if st[idx3] == 't':
#                                 st = st[idx3+1:]
#                                 for idx4 in range(len(st)):
#                                     if st[idx4] == 'o':
#                                         st = st[idx4+1:]
#                                         for idx5 in range(len(st)):
#                                             if st[idx5] == 'n':
#                                                   return True
#                                         return False
#                                 return False
#                         return False
#                 return False
#         return False
# print(' '.join(list(map(str, list(filter(lambda i:checker(lst[i-1]) is True,range(1, len(lst)+1)))))))
# #Ну или так :DDD:
# print(*[k + 1 for k in range(int(input())) if __import__('re').match(".*a.*n.*t.*o.*n.*", input())])

# import re
# st = input()+' запретил букву'
# b = ['а', 'б', 'в', 'г', 'д', 'е',
#      'ж', 'з', 'и', 'й', 'к', 'л',
#      'м', 'н', 'о', 'п', 'р', 'с',
#      'т', 'у', 'ф', 'х', 'ц', 'ч',
#      'ш', 'щ', 'ъ', 'ы', 'ь', 'э',
#      'ю', 'я']
# for i in range(len(b)):
#         if b[i] in st:
#             print((st +' '+ b[i]).lstrip())
#             st = ' '.join((''.join(re.split(f'{b[i]}', st))).split())






