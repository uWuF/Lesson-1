products = []
n, i,  = 1, 0
exit = 0
con = 0
name_analytics = []
price_analytics = []
count_analytics = []
unit_analytics = [0]

exit = input('Вы хотите начать?(y/n): ')
if exit == 'y':
    while con != 'n':
        products.append((n, {'Name': input("Введите название товара: "), 'Price': input("Введите стоимость товара: "),
                    'Count': input("Введите количество товара: "), 'Unit': input("Введите единицы товара: ")}))
        name_analytics.append(f"{products[i][1]['Name']}")
        price_analytics.append(f"{products[i][1]['Price']}")
        count_analytics.append(f"{products[i][1]['Count']}")
        unit_analytics.insert(0, (int(unit_analytics[0]) + int(f"{products[i][1]['Unit']}")))
        unit_analytics.pop(1)
        n, i = n + 1, i + 1
        con = input('Продолжить?(y/n): ')
        print('\n'.join(map(str, products)))

analytics = {'Name': name_analytics, 'Price': price_analytics, 'Count': count_analytics, 'Unit': unit_analytics}

print("Аналитика по товарам: ", analytics)
