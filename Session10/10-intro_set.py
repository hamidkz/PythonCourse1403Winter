numbers = [1, 3, 4, 9]
# Method 1
# while True:
#     user_number = input("Enter a number: ")
#     if int(user_number) == 99:
#         break
#     if int(user_number) not in numbers:
#         numbers.append(int(user_number))
#         print(numbers)

# Method 2
while True:
    user_number = int(input("Enter a number: "))
    numbers.append(user_number)
    numbers = list(set(numbers))
    print(numbers)


