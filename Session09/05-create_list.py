lst = [False, 'Iran', -1, 1000]
# output: Generate a list like lst_2 = [False, 'Iran', -1, 1000]

lst_2 = []
for item in lst:
    lst_2.append(item)
print(lst_2)

print(lst == lst_2)
print(lst is lst_2)

lst[0] = '*'
print(lst)
print(lst_2)

