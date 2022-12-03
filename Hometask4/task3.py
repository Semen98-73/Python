# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

from random import randint
rand_list = []
for _ in range(30):
    rand_list.append(randint(0, 100))
print(f'Список {rand_list}')

min_i = 0
for i in range(0, 30):
    for j in range(i + 1, 30):
        if rand_list[j] < rand_list[min_i]:
            min_i = j
    rand_list[i], rand_list[min_i] = rand_list[min_i], rand_list[i]

print(f'Отсортированный список {rand_list}')