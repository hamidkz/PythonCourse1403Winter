usernames = ["hamid.kz", "ali.2024", "hamid.kz"]

# Method 1
result = []
for username in usernames:
    result.append(f'{username}.gmail.com')
print(result)

# Method 2
result_2 = [f'{username}@gmail.com' for username in usernames]
print(result_2)

# Method 3
result_3 = map(lambda x: x+'@gmail.com', usernames)
print(set(result_3))