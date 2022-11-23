# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
    # for y in range(2):
       # for z in range(2):
            # if not (x or y or z) == (not x and not y and not z):
                # print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истенно при x = {x}, y={y}, z={z}')


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input('Введите X:'))
Y = int(input('Введите Y:'))

if X == 0 or Y == 0:
    print('X ≠ 0, Y ≠ 0')
elif X > 0 and Y > 0:
    print(f'x = {X}; y = {Y} -> 1 ')
elif X < 0 and Y > 0:
    print(f'x = {X}; y = {Y} -> 2 ')
elif X < 0 and Y < 0:
    print(f'x = {X}; y = {Y} -> 3 ')
elif X > 0 and Y < 0:
    print(f'x = {X}; y = {Y} -> 4 ')