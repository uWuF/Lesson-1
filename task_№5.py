gain = float(input('Введите прибыль фирмы: '))

spent = float(input('Введите траты фирмы: '))

a = gain - spent

b = 0

if a < 0:
    a = spent - gain
    print(f'Убыток составил {a} рублей.')
else:
    b = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на одного сотрудника составила: {a / b} рублей.')
