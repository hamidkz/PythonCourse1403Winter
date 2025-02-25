# Iran44 --> 44
# zapata1370a2 -- > 13702

text = "zapata1370a2"

result = ''
for char in text:
    if char.isnumeric():
        # result = result + char
        result += char

result = int(result)
print(result)


# Bad solution
# for char in text:
#     if char.isdigit():
#         print(char, end='')
