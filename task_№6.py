def my_func():
    for word in input('Введите слова через пробел маленькими латинскими буквами: ').split():
        a = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                a += 1
        if a == len(word):
            print(word.title())
        else:
            print(f'{word} - Вводите только маленькие буквы')


my_func()
