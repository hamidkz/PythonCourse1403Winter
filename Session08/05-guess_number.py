from random import randint

javaab = randint(1, 10)
# print(javaab)
for i in range(1,4):
    user_number = int(input(f"Enter your {i}th number:"))
    if user_number == javaab:
        print("Hooraaaa!")
        break
    elif user_number > javaab:
        print("Biaa paaeentar...")
    else:
        print("Boro balaatar...")
else:
    print("game over!")

# if i == 3 and user_number != javaab:
#     print("game over!")

