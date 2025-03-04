email = "hamid.kz@gmail.com"
# index of last dot: 14

# Method 1 (Good)
result_1 = email.rfind('.')
print(result_1)

# Method 2
last_dot_index = -1
for i in range(len(email)):
    if email[i] == '.':
        last_dot_index = i
print(last_dot_index)


