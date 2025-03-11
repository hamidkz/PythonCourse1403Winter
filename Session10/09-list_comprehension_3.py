# ['hmdf', 'hamid'] ae
# ['Hamid']

names = ['hmdf', 'hamid', 'z', 'ab']
result = [name.capitalize() for name in names if 'a' in name or 'e' in name]
print(result)
