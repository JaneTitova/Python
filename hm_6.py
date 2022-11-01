# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# ДЗ №2 - Задача №3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

num_e = 6
my_list = []
result = []
# dic_e = dict()         #Было так

# for i in range(1, num_e + 1):
#     dic_e[i] = round((1 + 1/i)**i, 2)
# print("Третья задача: Для n = ", num_e, ": ", dic_e)

my_list = [x for x in range(1, num_e + 1)]
my_list = list(map(lambda x: round((1 + 1/x)**x, 2), my_list))
result = list(enumerate(my_list))

print("Третья задача: Для n = ", num_e, ": ", result, ", сумма элементов : ", sum(my_list))

# ДЗ №3 - Задача №3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_3 = [1.1, 1.2, 3.1, 5, 10.01]

out = [x - x//1 for x in list_3 if x % 1]
min_fract = max_fract = out[0]

for i in out:
    if i < min_fract:
        min_fract = i

    if i > max_fract:
        max_fract = i

# min_fract = max_fract = list_3[0] - list_3[0]//1   
# for item in range(1, len(list_3)):          # Было так

#     fract_temp = list_3[item] - list_3[item]//1

#     if fract_temp < min_fract and fract_temp != 0:
#         min_fract = fract_temp

#     if fract_temp > max_fract:
#         max_fract = fract_temp

print('Третья задача. Разница между мах и мин значениями дробных частей :', list_3, ' => ' , round(max_fract - min_fract, 5))

# Совсем не густо получилось, в остальных случаях или не получается применить необходимые преобразования или мне кажется, они не упращают код.
