# d = dict([('foo', 100), ('bar', 200), ('baz', 300)])
# print(d)

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12],
#            'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19],
#            'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48],
#            'C9': [2, 7, 18, 28, 18, 28]}
#
# for k, v in my_dict.items():
#     my_dict[k] = list(filter(lambda x: x<=20,v))
# print(my_dict)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# l=[]
# for k, v in emails.items():
#     for el in v:
#         l.append(f'{el}@{k}')
# print(*sorted(l), sep='\n')

# DNK = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
# chain = list(input())
# new_chain=[]
# for el in chain:
#     new_chain.append(DNK[el])
# print(''.join(new_chain))

# s = input().split()
# d ={}
# a=[]
# for el in s:
#     d[el] = d.get(el, 0)+1
#     a.append(d[el])
# print(*a)

# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# word = list(input())
# sum=0
# for k, v in d.items():
#     for el in word:
#         if el in v:
#             sum+=k
# print(sum)

# def build_query_string(d):
#     l = ''
#     for k, v in sorted(d.items()):
#         l+=f'{k}={v}'
#         if len(d)>1:
#             l+='&'
#     return l[:-1]
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

# def merge(li):
#     di ={}
#     for d in li:
#         for k, v in d.items():
#             di[k] = di.get(k, set())
#             di[k].add(v)
#     return di
#
#
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

# s = {'write': 'W', 'read': 'R','execute': 'X'}
#
# n=int(input())
# files = [input().split() for _ in range(n)]
# files ={el[0]:el[1:] for el in files}
# m=int(input())
# ops = [tuple(input().split()) for _ in range(m)]
# for el in ops:
#     if s[el[0]] not in files[el[1]]:
#         msg = 'Access denied'
#     else:
#         msg = 'OK'
#     print(msg)

# n=int(input())
# line = [tuple(input().split()) for _ in range(n)]
# d={}
# for cst, good, cnt in list(sorted(line)):
#     d[cst]= d.get(cst, {})
#     # d[cst][good] = d[cst].get(good,0)+cnt
#     d[cst].update({good:d[cst].get(good,0)+int(cnt)})
# for k, v in d.items():
#     print(f'{k}:')
#     for ke, va in sorted(v.items()):
#         print(ke, va)
