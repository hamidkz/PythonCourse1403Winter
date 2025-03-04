import random

alphabets = "qwertyuioplkjhgfdsazxcvbnm"

result = ''
for i in range(10):
    ch_index = random.randint(0, len(alphabets) - 1)
    char = alphabets[ch_index]
    result += char

print(result)


