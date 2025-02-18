text = input("Enter your birthdate year:")
if text.isnumeric():
    year = int(text)
    age = 1403 - year
    print(age)