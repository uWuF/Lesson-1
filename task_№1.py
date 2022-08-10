def my_f(n_1, n_2):
    if n_2 == 0:
        print('Делить на 0 нельзя!')
        return
    result = n_1 / n_2
    print(result)


my_f(int(input('Введите числитель: ')), int(input('Введите знаминатель: ')))
