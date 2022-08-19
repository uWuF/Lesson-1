def fact(number):
    fact_number = 1
    for i in range(number + 1):
        yield f'{i}! = {fact_number}'
        fact_number *= i + 1


for el in fact(int(input('Factorial number: '))):
    print(el)
