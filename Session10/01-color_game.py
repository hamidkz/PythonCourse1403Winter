# ['R', 'G', 'B']
# G R B => False, False, True

import random

colors = ['R', 'G', 'B']
random.shuffle(colors)
# print('Javab: ', colors)

for index in range(3):
    user_input = input("Enter your choices: ")
    user_input_list = list(user_input.upper()) # ['R', 'G', 'B']
    check_list = [
        user_input_list[0] == colors[0],
        user_input_list[1] == colors[1],
        user_input_list[2] == colors[2],
    ]
    if check_list == [True, True, True]:
        print("Hooraaayyy!!!!")
        break
    else:
        print(check_list)
        print('Try again!')