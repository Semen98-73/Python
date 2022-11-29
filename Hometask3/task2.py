# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

str = input('Введите строку: ')
try:
    float(str)
    if str.find('.') != -1 and str.count('.') == 1:
        print('Дробное число')
    else:
        raise ValueError
except ValueError:
    print('Не дробное число')
