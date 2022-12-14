# 1) Сделать игру морской бой

from random import randint

sea = [['.\t' for _ in range(4)] for _ in range(4)]

def show_buttlefield():
    for e in sea:
        for j in e:
            print(j, end='')
        print()


show_buttlefield()

ships = [(randint(0, 2), randint(0, 2))]
while len(ships) < 2:
    ship = (randint(0, 2), randint(0, 2))
    if ship not in ships:
        ships.append(ship)

ship_count = len(ships)
torpedo_count = 0
previous_shots = []


def check_range(coordinates):

    while len(coordinates) < 3:
        coordinates = input('Координаты должны состоять из 2 значений! Повтори ввод: ')

    spl = coordinates.split()
    tup = tuple(map(int, spl))  

    while tup[0] > 3 or tup[1] > 3:
        new_input = input('Координаты должны быть в диапазоне от 0 до 4! Повтори ввод: ')
        tup = check_range(new_input)

    return tup


while ship_count:
    user_try = input('\nТвой выстрел! Введите координаты от 0 до 4 через пробел: ')
    user_try = check_range(user_try)
    if user_try in previous_shots:
        print('Такой выстрел уже был!')
    elif user_try in ships:
        ship_count -= 1
        sea[user_try[0]][user_try[1]] = '[X]\t'
        print(f'Попал! Осталось {ship_count} кораблей.')
    else:
        sea[user_try[0]][user_try[1]] = '*\t'
        print(f'Мимо!')
    torpedo_count += 1
    previous_shots.append(user_try)
    show_buttlefield()
else:
    print(f'\nПобеда! Все корабли противника потоплены!')
