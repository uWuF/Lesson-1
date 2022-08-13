def info(**kwargs):
    return ' '.join(kwargs.values())


print(info(name=input('Введите своё имя: '), surname=input('Введите свою фамилию: '),
           year=input('Введите год рождения: '), city=input('В каком городе вы живёте: '),
           email=input('Напишите свою электронную почту: '), phone=input('Напишите свой номер телефона: ')))
