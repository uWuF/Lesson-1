number = int(input("Введите время в секундах: "))

hour = number // 3600

minute = (number - ((number // 3600) * 3600)) // 60

second = number - (((number // 3600) * 3600) + (minute * 60))

print(f"{hour:02}:{minute:02}:{second:02}")
