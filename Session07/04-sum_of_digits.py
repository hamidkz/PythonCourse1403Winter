
num = input("Enter your number:")
# input: 123 -> result = 6 

result = 0
for digit in num:
    result += int(digit)
print(result)
