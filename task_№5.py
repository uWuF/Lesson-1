def my_func():
    sum_of_num = 0
    while True:
        err = False
        numbers = input('Введите целые числа через пробел, для выхода введите q: ').split()
        for i in numbers:
            if i == 'q':
                return sum_of_num
            else:
                try:
                    sum_of_num += int(i)
                except ValueError:
                    err = True
        if err:
            print('Вводите только целые числа!')
        print(f'Сумма введённых чисел: {sum_of_num}')


print(my_func())
