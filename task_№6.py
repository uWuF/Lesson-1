from itertools import count, cycle

my_list = ['A', 'B', 'C']

for i in count(3):
    print(i, end=' ')
    if i >= 10:
        print()
        break

for x, y in enumerate(cycle(my_list)):
    print(y, end=' ')
    if x >= 10:
        break
