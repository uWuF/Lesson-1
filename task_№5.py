from functools import reduce

my_list = [i for i in range(100, 1001, 2)]

multip = reduce(lambda x, y: x * y, my_list)

print(my_list)

print(f'Результат перемножения чисел - {multip}')
