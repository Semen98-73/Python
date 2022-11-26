#  1) Вводим с клавиатуры целое число X и У.
#  Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

num = int(input("Введите первое число X: "))
num2 = int(input("Введите второе число Y: "))
count = 0
if num < num2:
    for i in range(num + 1, num2):
        if i % 2 == 0 and i % 3 == 0:
            count += 1
    print(count)
elif num2 < num:
    for i in range(num2 + 1, num):
        if i % 2 == 0 and i % 3 == 0:
            count += 1
    print(count)
