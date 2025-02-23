number_1 = input("Enter first number:")
number_2 = input("Enter second number:")
operator = input("Enter operator:")

if operator in "+=*/" and number_1.isnumeric() and number_2.isnumeric():
    number_1 = int(number_1)
    number_2 = int(number_2)
    if operator == '+':
        print(number_1 + number_2)
    elif operator == '-':
        print(number_1 - number_2)
    elif operator == '/':
        print(number_1 / number_2)
    else:
        print(number_1 * number_2)
else:
    print("Sorry")

match operator:
    case '+':
        print(number_1 + number_2)
    case '-':
        print(number_1 - number_2)
    case '/':
        print(number_1 / number_2)
    case '*':
        print(number_1 * number_2)
    case _:
        print("Sorry")

