n = int(input('Введите число: '))

a = n % 10

b = 0

while n > 0:
    b = (n // 10) % 10
    n = n // 10
    if b > a:
        a = b
print(a)
