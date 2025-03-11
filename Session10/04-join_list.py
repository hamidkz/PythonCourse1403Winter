list_1 = [1, 2, 3]
list_2 = [4, 5]
# output: [1, 2, 3, 4, 5]

# Method 1
result = []
for item in list_1:
    result.append(item)
for item in list_2:
    result.append(item)
print(result)

# Method 2
result_2 = list_1 + list_2
print(result_2)

# Method 3
result_3 = []
result_3.extend(list_1)
result_3.extend(list_2)
print(result_3)

# Method 4
result_4 = [*list_1, *list_2]
print(result_4)