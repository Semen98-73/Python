weekdays = {1: 'MN.txt', 2: 'TUE.txt', 3: 'WED.txt', 4: 'THU.txt', 5: 'FR.txt', 6: 'SAT.txt', 7: 'SUN.txt'}

schedule_change = int(input('Enter 1 to read, 2 - to add, 3 - to change: '))
while schedule_change < 1 or schedule_change > 3: 
    schedule_change = int(input('Error. Try again (1, 2 or 3): '))

if schedule_change == 1:
    day = int(input('Enter day of week (from 1 to 7): '))
    with open(weekdays[day], 'r', encoding='utf-8') as my_f:
        print(my_f.readlines())

elif  schedule_change == 2:
    day = int(input('Enter day of week (from 1 to 7): '))
    event = input('What event would U like to add? ')
    with open(weekdays[day], 'a', encoding='utf-8') as my_f:
        my_f.write(event)
        my_f.write('\n')

elif  schedule_change == 3:
    day = int(input('Enter day of week (from 1 to 7): '))
    event = input('What event would U like to add? ')
    with open(weekdays[day], 'w', encoding='utf-8') as my_f:
        my_f.write(event)
        
        