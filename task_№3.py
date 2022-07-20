seasons = ['winter', 'spring', 'summer', 'fall']

number = int(input('Введите число от 1 до 12: '))

if number == 12 or number <= 2:
    print(seasons[0])
elif 2 < number < 6:
    print(seasons[1])
elif 5 < number < 9:
    print(seasons[2])
elif 8 < number < 12:
    print(seasons[3])
else:
    print('Неверное число')

seasons = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'fall', 10: 'fall', 11: 'fall'}

number = int(input('Введите число от 1 до 12: '))

print(seasons.get(number))
