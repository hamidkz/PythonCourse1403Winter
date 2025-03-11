lst = ['Hamid', 'Vahid', 'Hamid', 'Zahra', 'Mina'] # Iterable 
index = 0
for name in lst:
    print(index, name)
    index += 1
print('---------------')
for i, name in enumerate(lst):
    print(i, name)


