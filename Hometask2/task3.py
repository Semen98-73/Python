# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

num = int(input("Введите зарплату: "))
num2 = int(input("Введите номинал купюры: "))
a = 0
b = 0
c = 0
d = 0
if num2 == 25:
    while num >= 25:
        num -= 25
        a += 1
    print(a)
if num2 == 10:
    while num >= 10:
        num -= 10
        b += 1
    print(b)
if num2 == 3:
    while num >= 3:
        num -= 3
        c += 1
    print(c)
if num2 == 1:
    while num >= 1:
        num -= 1
        d += 1
    print(d)
if num2 != 25 and num2 !=10 and num2 !=3 and num2 !=1:
  print("Таких купюр нет")
  
