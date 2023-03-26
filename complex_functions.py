import re
import operator as o
import colorama
from colorama import Fore, Back, Style
import math

colorama.init(autoreset=True)


expl = '(33/3)+(10+(3*2))-22*11'
expl2 = '(-6/3)'
expl3 ='4+3*(9-1)-10*((2+1)*2)'
expl4 = '1*(-1-9)'
expl5 = '(33/3)+(10+(3*2))-22*11+4+3*(9-1)-10*((2+1)*2)+10'

class Solver():

    def solve(self, line:str)->float:
        if self.__check_correct_brackets(line):

            line = self.__get_log(line)
            line = self.__get_exp(line)
            line = self.__get_pow(line)

            while re.findall(r'[\(\)]', line):
                if re.findall(r'[\+\-\*\/]', line):
                    self.__new_line = re.split(r'(\(\-?\d*\.?\d*[\+\-\*\/]\d*\.?\d*\))', line)
                    line = re.split(r'\(\-?\d*\.?\d*[\+\-\*\/]\d*\.?\d*\)', line)
                    self.__el = re.sub(r'[\(\)]', '',
                                       list(set(self.__new_line) - set(line))[0])
                    num = self._calculate_expression(self.__el)
                    self.__new_line[self.__new_line.index('(' + self.__el + ')')] = str(num)
                    line = ''.join(self.__new_line)
                else:
                    return float(re.sub(r'[\(\)]', '', line))
                if not re.findall(r'[\+\-\*\/]', line):
                    return float(line)
            return self._calculate_expression(line)
        else:
            raise ValueError('Non correct usage of brackets')

    def __check_correct_brackets(self, line:str)->bool:
        stack = []
        for el in line:
            if el == '(':
                stack.append(el)
            elif el == ')' :
                if stack == []:
                    return False
                else:
                    last = stack.pop()
                    if last !='(':
                        return False
        return True if stack == [] else False

    def __check_one_value(self, line):
        return re.search(r'\-?\d+\.?\d*', line).group() == line

    def __get_log(self, line):
        arr_val = re.split(r'([\+\-\*\/])', line)
        for idx, el in enumerate(arr_val):
            if el in re.findall(r'log\(\-?\d*\.?\d*\,\-?\d*\.?\d*\)', line):
                a, b = tuple(re.findall(r'\-?\d+\.?\d*', el))
                arr_val[idx] = str(math.log(float(a), float(b)))
        return ''.join(arr_val)

    def __get_exp(self, line):
        arr_val = re.split(r'([\+\-\*\/])', line)
        for idx, el in enumerate(arr_val):
            if el in re.findall(r'exp\(\-?\d*\.?\d*\)', line):
                e = re.search(r'\-?\d+\.?\d*', el).group()
                arr_val[idx] = str(math.exp(float(e)))
        return ''.join(arr_val)

    def __get_pow(self, line):
        arr_val = re.split(r'(\-?\(?\-?\d+\.?\d*\)?\*\*\-?\(?\-?\d+\.?\d*\)?)', line)
        if arr_val:
            for i in range(1, len(arr_val), 2):
                a, b = re.findall(r'\-?\d+\.?\d*', arr_val[i])
                arr_val[i] = str(float(a)**float(b))
        return ''.join(arr_val)

    def _calculate_expression(self, line:str)->float:
        if self.__check_one_value(line):
            return float(line)
        line = re.sub(r'\-', '+-', line)
        if line[0]=='+': line = line[1:]
        opers = re.split(r'\-?\d+\.?\d*', line)[1:-1]
        missed_value = ''
        idx = 0
        while opers:
            nums = re.split(r'[\*\/\+]', line)
            if '*' in opers:
                idx = opers.index('*')
                missed_value = float(nums[idx]) * float(nums[idx + 1])
            elif '/' in opers:
                idx = opers.index('/')
                missed_value = float(nums[idx]) / float(nums[idx + 1])
            elif '-' in opers:
                idx = opers.index('-')
                missed_value = float(nums[idx]) - float(nums[idx + 1])
            elif '+' in opers:
                idx = opers.index('+')
                missed_value = float(nums[idx]) + float(nums[idx + 1])

            opers.pop(idx)
            if not opers:
                return missed_value
            nums = nums[:idx] + [missed_value] + nums[idx + 2:]
            nums = [str(el) for el in nums]
            line = ''.join([''.join([x, y])
                            for x, y in zip(nums, opers)] + [nums[-1]])
        return missed_value


solv = Solver()

a = solv.solve(expl5)
print('a = ', a)

b = solv.solve('10+log(8.0,2.1)')
print('b = ', b)

c= solv.solve('10+exp(2)')
print('c = ', c)

d= solv.solve(expl5+'+10**(2)+10**(3)+log(8.0,2.0)')
print('d = ', d)

e = solv.solve('(-3-10)*2')

print(Fore.LIGHTGREEN_EX+'e = '+str(e))