
num = input("Enter your number:")
# 734129 -> 6

result = 0
# for digit in num:
#     d = int(digit)
#     if d % 2 == 0:
#         result += d
# print(result)

for digit in num:
    result += int(digit) if int(digit) % 2 == 0 else 0
print(result)
