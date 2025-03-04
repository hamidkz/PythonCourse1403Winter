import random

# length = int(input("Enter your password length:"))
length = 10

alphabets = "qwertyuioplkjhgfdsazxcvbnm1234567890"
special_chars = "!@#$%^&"

password = ''
for i in range(8):
    char_index = random.randint(0, len(alphabets) - 1)
    char = alphabets[char_index]
    shir_yaa_khat = random.randint(0,1)
    if shir_yaa_khat == 0:
        char = char.upper()
    password += char

for i in range(2):
    char_index = random.randint(0, len(special_chars) - 1)
    char = special_chars[char_index]
    password += char

print(password)



