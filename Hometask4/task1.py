# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
number = int(input('Введите размер списка: '))
rand_list = []
sum = 0
for i in range(number):
    rand_list.append(randint(0, 100))
    if i % 2 != 0:
      sum += rand_list[i]

print(rand_list)
print(f'Сумма чисел стоящих на нечётной позиции равна {sum}')
