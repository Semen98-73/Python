# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

a = input("Введите многозначное число: ")

for i in range(len(a)):
    if a[i] > a[i-1]:
        i += 1
        b = "Да"
    else:
        b = "Нет"
print(b)

# вот с этим условием в скобках ( 1 меньше 5, 5 меньше 7, а 7 меньше 9) не очень понял как выводить именно каждую цифру и писать какая цифра меньше,
#  если бы количество чисел было бы одинаковое,
# то в print можно было написать как то так , а с любым числом не очень понял как надо, а без этого условия программа работает  
 
# print(f'{a} - {b} ( {a[0]} меньше {a[1]}, {a[1]} меньше {a[2]}, а {a[2]} меньше {a[3]} )')