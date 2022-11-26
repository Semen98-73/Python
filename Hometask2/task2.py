# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

num = int(input("Введите число X: "))
firstmax = 0
secondmax = 0
for i in range(num):
    a = int(input(f'Введите {num} числа(ел): '))
    if a > firstmax:
        secondmax = firstmax
        firstmax = a
    elif secondmax < a:
        secondmax = a
print(firstmax)
print(secondmax)
