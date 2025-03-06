lst = []
for i in range(10):
    lst.append(i)
    print(f'{i} append to list. list is: {lst}')

import random
alphabets = 'qwertgfdsa'
lst_2 = []
for i in range(3):
    lst_2.append(alphabets[random.randint(1, len(alphabets))])
print(lst_2)
