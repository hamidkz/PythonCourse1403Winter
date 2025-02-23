# Ternary operator

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

if num_1 > num_2:
    max = num_1
    # print(num_1)
else:
    max = num_2
    # print(num_2)
print(max)

max_2 = num_1 if num_1 > num_2 else num_2
print(max_2)