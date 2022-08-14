from sys import argv


def salary():
    try:
        time, money_per_hour, bonus = map(float, argv[1:])
        print(f'Salary - {time * money_per_hour + bonus}')
    except ValueError:
        print('Вводите только числа!')


salary()
