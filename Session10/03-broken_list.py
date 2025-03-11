lst = [1,2,3,4, 5]
# output: [1,2,3] [4,5]

list_1 = []
list_2 = []

center_index = int(len(lst) / 2)
for i in range(len(lst)):
    if i < center_index:
        list_1.append(lst[i])
    else:
        list_2.append(lst[i])

print(list_1, list_2)
