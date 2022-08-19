my_list = [0, 0, 0, 44, 5, 21, -2, -1]

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(new_list)
