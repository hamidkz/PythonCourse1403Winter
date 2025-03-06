text = 'game of Thrones'
# output: #game_of_thrones

# Method 1
result_1 = '#' + text.replace(' ', '_')
print(result_1)

# Method 2
lst = text.split(' ')
for word in lst:
    for i in range(len(lst - 1)):
        l
result_2 = '#' + '_'.join(lst)
print(result_2)