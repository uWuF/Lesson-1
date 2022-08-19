my_list = list(map(int, (input('Введите целые числа через пробел: ').split())))

print(my_list)

my_list_copy = []

for i in range(len(my_list)):
    if my_list[i] not in my_list_copy:
        my_list_copy.append(my_list[i])

for i in range(len(my_list_copy)):
    if my_list_copy[i] in my_list:
        my_list.remove(my_list_copy[i])

new_list = [my_list_copy[num] for num in range(len(my_list_copy)) if my_list_copy[num] not in my_list]

print(new_list)
