lst = [2, 4, 'iran', '*', 2, 5, '*', 4]
# output: [2, 4, 'iran', '*', 5]

result = []
for item in lst:
    if item not in result:
        result.append(item)
print(result)


