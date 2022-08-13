def my_func():
    word = input('Введите слово маленькими латинскими буквами: ')
    a = 0
    for i in word:
        if 97 <= ord(i) <= 122:
            a += 1
    if a == len(word):
        print(word.title())
    else:
        print(f'{word} - Вводите только маленькие латинские буквы')


my_func()
