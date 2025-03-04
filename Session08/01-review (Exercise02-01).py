text = "Welcome to Iran"
# output: e (2)

max_repeat = 0
max_repeat_char = ''

for char in text:
    repeat_times = text.count(char) # l: repeat_times = 1
    if repeat_times > max_repeat: # F
        max_repeat = repeat_times # max_repeat: 2
        max_repeat_char = char # max_repeat_char: e
print(max_repeat_char, '(', max_repeat, ')')
