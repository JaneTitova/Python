# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_1 = [2, 3, 5, 9, 3]
summ_odd_symb = 0

for item in range(1, len(list_1), 2):
    summ_odd_symb += list_1[item]

print('Первая задача. У списка: ', list_1, ' сумма нечетных элементов - ', summ_odd_symb)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_2 = [2, 3, 4, 5, 6]
list_mult = []

for item in range(len(list_2)//2):
    list_mult.append(list_2[item] * list_2[-1 - item])

if len(list_2) % 2:
    list_mult.append(list_2[len(list_2)//2] **2) 

print('Вторая задача. (попарное произведение) ', list_2, ' => ', list_mult)

# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_3 = [1.1, 1.2, 3.1, 5, 10.01]
# не успела поискать как лучше определить 2 переменные одним значение, посмотрю!
min_fract = list_3[0] - list_3[0]//1   
max_fract = min_fract

for item in range(1, len(list_3)):

    fract_temp = list_3[item] - list_3[item]//1

    if fract_temp < min_fract and fract_temp != 0:
        min_fract = fract_temp

    if fract_temp > max_fract:
        max_fract = fract_temp

print('Третья задача. Разница между мах и мин значениями дробных частей :', list_3, ' => ' , round(max_fract - min_fract, 5))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num_d = 45
num_for_print = num_d
num_double = ""

while num_d:
    num_double = str(num_d % 2) + num_double
    num_d //= 2

print('Четвертая задача. Из десятичного в двоичное. ', num_for_print, ' => ', num_double)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
print('пятая задача. Решаю рекурсией:')

def fib(x):
    if x in [-1, 1]:
        return 1
    elif x == 0:
        return 0
    elif x > 1:
        return fib(x - 1) + fib(x - 2)
    elif x < -1:
        return fib(x + 2) - fib(x + 1)

for item in range(-8, 9):
    print(fib(item))

# второй вариант не рекурсией

list_fib = [0, 1]
my_num = 8

for item in range(-my_num, my_num + 1):
    if item < 0:
        list_fib.insert(0, list_fib[1] - list_fib[0])
    elif item > 1:
        list_fib.append(list_fib[item - 1 + my_num] + list_fib[item - 2 + my_num])


print('пятая задача. Решаю списком:', list_fib)
