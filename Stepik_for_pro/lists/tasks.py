# letters = ['a', 'b', 'c', 'd']
# print(list(letters))

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for el in list1:
#     maximum  = max(el) if max(el)>maximum else maximum
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#
# for el in list1:
#     el.reverse()
#
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# print(sum(list(map(sum, list1)))/sum(list(map(len, list1))))

# list1 = [[1] * 3] * 3
# list1[0][1] = 5
# print(list1)

# n=int(input())
# for i in range(n):
#     print([i for i in range(1, n+1)], end='')
#     print()

# n=int(input())
# for i in range(1, n+1):
#     print([i for i in range(1, i+1)], end='')
#     print()

# num=int(input())
# def pascal(n):
#     li = [([1]+[0 for i in range(1, n+1)]) for _ in range(1, n+2)]
#     if n==0:
#         return [1]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             li[i][j] = li[i-1][j]+li[i-1][j-1]
#     return li[n]
#
#
# print(pascal(num))

# num=int(input())
# def pascal(n):
#     li = [([1]+[0 for i in range(1, n)]) for _ in range(1, n+1)]
#     for i in range(1, n):
#         for j in range(1, n):
#             li[i][j] = li[i-1][j]+li[i-1][j-1]
#
#     for i in range(n):
#         print(' '.join(list(map(str, list(filter(lambda x: x!=0, li[i]))))), end='')
#         print()
#
# pascal(num)

# li = [i for i in input().split()]
# prli =[[li[0]]]
# for i in range(1, len(li)):
#     print(prli)
#     if li[i] == li[i-1]:
#         prli[len(prli)-1].append(li[i])
#     else:
#         prli.append([li[i]])
# print(prli)

# lst = [i for i in input().split()]
# ch = int(input())
# def chunked(li, ch_len):
#     chnk = [[] for _ in range(len(li)//ch_len)]
#     for i in range(len(chnk)):
#         for j in range(ch_len):
#             chnk[i].append(li[i*ch_len+j])
#     if len(li)%ch_len!=0:
#         chnk.append([li[j] for j in range(ch_len*len(chnk), len(li))])
#     return chnk
#
# print(chunked(lst, ch))

# li = [i for i in input().split()]
# pod_li=[[]]
# for i in range(len(li)+1):
#     for j in range(i):
#         pod_li.append(li[j:i])
#         pod_li.sort(key = lambda x:len(x))
# print(pod_li)



