def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(my_list))
    return sum(my_list)


print(my_func(float(input('Первое число: ')),
              float(input('Второе число: ')),
              float(input('Третье число: '))))
