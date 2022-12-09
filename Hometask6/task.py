from random import randint


sea = [['.\t' for _ in range(5)] for _ in range(5)]

def show_buttlefield():
    for e in sea:
        for j in e:
            print(j, end='')
        print()


show_buttlefield()


def second_square(x, y, direction):
    if direction == 1:
        if y + 1 >= len(sea) or [x, y + 1] in double_ships:
            return second_square(x, y, 2)
        else:
            return [x, y + 1]
    if direction == 2:
        if x + 1 >= len(sea) or [x + 1, y] in double_ships:
            return second_square(x, y, 3)
        else:
            return [x + 1, y]
    if direction == 3:
        if y - 1 < 0 or [x, y - 1] in double_ships:
            return second_square(x, y, 4)
        else:
            return [x, y - 1]
    if direction == 4:
        if x - 1 < 0 or [x - 1, y] in double_ships:
            return second_square(x, y, 1)
        else:
            return [x - 1, y]




double_ships = []
used_squares = []



while len(double_ships) < 2:
    
    ship = {
        'square1': [],
        'square2': [],
        'hits': 0  
    }

   
    x, y = randint(0, 4), randint(0, 4)
    if [x, y] not in used_squares:
        direction = randint(1, 4)  

        ship['square1'] = [x, y]
        used_squares.append(ship['square1'])
        ship['square2'] = second_square(x, y, direction)
        used_squares.append(ship['square2'])
        double_ships.append(ship)


single_ships = []
while len(single_ships) < 4:
    s_ship = [randint(0, 4), randint(0, 4)]
    if s_ship not in used_squares:
        single_ships.append(s_ship)
        used_squares.append(s_ship)

ship_count = len(single_ships) + len(double_ships)
torpedo_count = 0
previous_shots = []


def check_errors(coordinates):
    while len(coordinates) < 3:
        coordinates = input('Координаты должны состоять из 2 значений! Повтори ввод: ')

    spl = coordinates.split()
    li = list(map(int, spl))  
  
    while li[0] > 4 or li[1] > 4:
        new_input = input('Координаты должны быть в диапазоне от 0 до 4! Повтори ввод: ')
        li = check_errors(new_input)

    return li


while ship_count:
    user_try = input('\nТвой выстрел! Введи координаты от 0 до 4 через пробел: ')
    user_try = check_errors(user_try)

    if user_try in previous_shots:
        print('Такой выстрел уже был!')
        torpedo_count += 1
        continue
    elif user_try not in used_squares:
        sea[user_try[0]][user_try[1]] = '*\t'
        print('Промах!')
    elif user_try in single_ships:
        ship_count -= 1
        sea[user_try[0]][user_try[1]] = '[X]\t'
        print(f'Убит! Осталось кораблей: {ship_count}.')
    else:
        for el in double_ships:
            if user_try in el.values():
                sea[user_try[0]][user_try[1]] = '[X]\t' 
                el['hits'] += 1
                if el['hits'] == 2:
                    ship_count -= 1
                    print(f'Убит! Осталось кораблей: {ship_count}.')
                else:
                    print('Ранен!')

    torpedo_count += 1
    previous_shots.append(user_try)
    show_buttlefield()
else:
    print(f'\nПобеда! Все корабли противника затоплены!\n'
          f'Расход {torpedo_count} торпед')