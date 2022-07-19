my_str = input('Введите строку: ')

b = 1

for i in (my_str.split(' ')):
    print(f"{b}.", i[:10])
    b += 1
