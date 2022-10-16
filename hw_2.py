# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

my_num = 1.567
my_num_safe = my_num
summ_of_digits = 0

# если не целое, делаем целым
while my_num % 1:
    my_num*= 10

# если число отрицательное, то деление на 10 отрабатывает не так, как я представляла, интересно так, наоборот)
if my_num < 0:    
    my_num*= -1

while my_num % 10:
    summ_of_digits+= my_num % 10
    my_num//= 10

# второй вариант
lst_sum = list(str(my_num_safe))
summ_of_digits_2 = 0
print(lst_sum)

for i in lst_sum:
    if i.isdigit():
        summ_of_digits_2 += int(i)


print("Первая задача: ", my_num_safe, " -> ", round(summ_of_digits))
print("Первая задача: (второй варинат) ", my_num_safe, " -> ", summ_of_digits_2)

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num_f = 4
factorial_my = 1
lst_f = [1]

for i in range(2, num_f + 1):
    factorial_my*= i
    lst_f.append(factorial_my)

print("Вторая задача: N = ", num_f, ", тогда ", lst_f)

# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

num_e = 6
dic_e = dict()

for i in range(1, num_e + 1):
    dic_e[i] = round((1 + 1/i)**i, 2)

print("Третья задача: Для n = ", num_e, ": ", dic_e)

# 4 - Алгоритм перемешивания списка

lst_for_mess = [2, 567, 56, 149, 8, 46, 102, -3, 55]
half_of_len = len(lst_for_mess)//2
temp = None
random_bit = False

print("Четвертая задача:")
print("До:")
print(lst_for_mess)

# меняю местами половины списка
for i in range(0, half_of_len):
    temp = lst_for_mess[i]
    lst_for_mess[i] = lst_for_mess[i - half_of_len]
    lst_for_mess[i - half_of_len] = temp

# кручу-верчу запутать хочу, есть некая булевая переменная,
# которая принимает своё значение из сравнения папарно элементов,
# она же опряделяет какое сравнени будет приниматься на следующем шаге.
for i in range (0, len(lst_for_mess) - 1, 2):
    for j in range (1, len(lst_for_mess), 2):
        if random_bit:
            if lst_for_mess[i] > lst_for_mess[j]:
                temp = lst_for_mess[i]
                lst_for_mess[i] = lst_for_mess[j]
                lst_for_mess[j] = temp
                random_bit = False
            else:
                random_bit = True
        else:
            if lst_for_mess[i] < lst_for_mess[j]:
                temp = lst_for_mess[i]
                lst_for_mess[i] = lst_for_mess[j]
                lst_for_mess[j] = temp
                random_bit = True
            else:
                random_bit = False

# и перевернули (взболтать, но не перемешивать))
lst_for_mess.reverse()
print("После:")
print(lst_for_mess)