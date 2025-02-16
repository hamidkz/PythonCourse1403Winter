""" شبیه سازی Capitalize """

# input: hamid -> output: Hamid

name = input("Enter your name:")
first_char = name[0]
remain = name[1:]

result = f"{first_char.capitalize()}{remain}"
print(result)

