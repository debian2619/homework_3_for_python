# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
origin_list = [1.1, 1.2, 3.1, 5, 10.01]
max_= 0
min_ = 0
current = 0
for i in range(len(origin_list)):
    current = origin_list[i] % 1
    if current != 0:
        if current > max_:
            max_ = current
        elif current < min_:
            min_ = current

print(current)