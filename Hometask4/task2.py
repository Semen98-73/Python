# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint
a = int(input('A = '))
b = int(input('B = '))
ab_list = []
for index in range(a):
    ab_list.append([])
    for value in range(b):
        ab_list[index].append(randint(1, 10))

print('Среднее - арифметическое каждой строки: ')
for i in range(a):
    b_sum = 0
    for j in range(b):
        b_sum += ab_list[i][j]
    print(f'{i+1} Строка  {ab_list[i]} - {round(b_sum / b, 2)}')