# 1) Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной продукт
#  к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup:
    def __init__(self, name, product = ''):
        self.product = product
        self.name = name
    
    def show_my_soup(self):
        if self.product == '': print(f'{self.name} - just to add hot water')
        else: print(f'{self.name} - {self.product}')

noodle_soup = Soup('Noodle soup','noodle')
hot_cup = Soup('Hot cup')

noodle_soup.show_my_soup()
hot_cup.show_my_soup()