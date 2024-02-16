import random


def get_random_value(lst):
    return random.choice(lst)


my_list = [n for n in range(1, 101)]

new_list = []

for i in range(1, 101):
    new_list.append(get_random_value(my_list))


print(new_list)


