# hamid.kz@gmail.com --> h****************m

text = 'hamid.kz@gmail.com'

# Method 1 : Best
result = text[0] + (len(text) - 2) * '*' + text[-1]
print(text)
print(result)

# Method 2
# index = 0
# result = ''
# for ch in text:
#     print(index, ch)
#     if index == 0 or index == len(text) - 1:
#         result += ch
#     else:
#         result += '*'
#     index += 1
# print(text)
# print(result)

# Method 3
# result = text[0]
# for ch in text[1:-1]:
#     result = result + '*'
# result = result + text[-1]
# print(text)
# print(result)