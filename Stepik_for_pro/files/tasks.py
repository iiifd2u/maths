# name = input()
# file = open(f'{name}')
# for line in file.readlines():
#     print(line.strip())
# file.close()

# name = input()
# file = open(f'{name}')
# print(file.readlines()[-2].strip())
# file.close()


# import random
# file = open('lines.txt', encoding='utf-8')
# print(random.choice(file.readlines()).strip())
# file.close()

# file = open('numbers.txt', encoding='utf-8')
# sum = 0
# for line in file.readlines():
#     sum+=int(line.strip())
#
# print(sum)

# file = open('nums.txt', encoding='utf-8')
# sum = 0
# for line in file.read().split():
#     sum+=int(line.strip())
#
# print(sum)

# file = open('prices.txt', encoding='utf-8')
# sum=0
# for line in file.readlines():
#     l=[el.strip() for el in line.split('\t')]
#     sum+=int(l[1])*int(l[2])
# print(sum)
# file.close()

num = int('1000001', 2)
print(num)