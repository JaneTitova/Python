# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math as m

d = 4

print('Первая задача')
print(round(m.pi, d))
print(str(m.pi)[:2 + d])

# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def is_simple(n):
    k = 0 
    for i in range(2, n // 2 + 1):
        if not n % i:
            k += 1
            return False
    if k == 0:
        return True

def list_of_simple (n):
    simple_list = []
    for i in range(2, n // 2 + 1):
        if not n % i:
            if is_simple(i):
                simple_list.append(i)
    return simple_list


numb = 12
print('Вторая задача')
print(list_of_simple(numb))

# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [2, 2, 3, 6, 3, 7, 2]
my_set = set()
my_set_double = set()

for i in my_list:
    len_set = len(my_set)
    my_set.add(i)
    if len_set == len(my_set):
        my_set_double.add(i)

my_set = my_set.difference(my_set_double)

print('Третья задача')
print(my_set)

# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

print('Четвертая задача')
k = 2
my_dic_4 = dict()
str_dic = ' = 0'

for i in range(k + 1):
    # 'x**' + str(i)
    my_dic_4['x**' + str(i)] = random.randint(0, 100)

print(my_dic_4)

for item in my_dic_4.items():
    if item[1] != 0:
        if item[0] == 'x**0':
            str_dic = ' + ' + str(item[1]) + str_dic
        else:
            str_dic = ' + ' + str(item[1]) + str(item[0]) + str_dic

str_dic = str_dic[3:]

print(str_dic)

data = open('file3_4.txt', 'w')
data.write(str_dic)
data.close()

# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
def split_str(my_str):
    my_dic = dict()
    my_list = []
    my_str = my_str[:-4]
    my_list = my_str.split(' + ')
    for i in my_list:
        if 'x**' in i:
            my_dic['x**' + i[-1]] = i[:-4]
        else:
            my_dic['x**0'] = i
    return my_dic


print('Пятая задача')
str_1 = ''
str_2 = ''
str_new = ' = 0'
dic_1 = dict()
dic_2 = dict()
dic_new = dict()

data = open('file3_4.txt', 'r')
for line in data:
    str_1 += line
data.close()

data = open('file_1.txt', 'r')
for line in data:
    str_2 += line
data.close()

dic_1 = split_str(str_1)
dic_2 = split_str(str_2)

for i in dic_1.items():
    for j in dic_2.items():
        if i[0] == j[0]:
            dic_new[i[0]] = int(i[1]) + int(j[1])

for item in dic_new.items():
    if item[1] != 0:
        if item[0] == 'x**0':
            str_new = ' + ' + str(item[1]) + str_new
        else:
            str_new = ' + ' + str(item[1]) + str(item[0]) + str_new

str_new = str_new[3:]

data = open('file3_5.txt', 'w')
data.write(str_new)
data.close()

print(str_1)
print(str_2)

print(dic_1)
print(dic_2)
print(dic_new)
