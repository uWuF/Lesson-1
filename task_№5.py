number = int(input('Введите число: '))

my_list = [number]

print(my_list)

n = 0

while n != 999:
    n = int(input('Введите число (для завершения программы введите 999): '))
    if n in my_list:
        my_list.insert((my_list.index(n) + my_list.count(n)), (n))
    elif n > my_list[0]:
        my_list.insert(0, n)
    elif n < my_list[-1]:
        my_list.append(n)
    else:
        for i in range(len(my_list)):
            if my_list[i] > n and my_list[i + 1] < n:
                my_list.insert(i + 1, n)

    print(my_list)
