# List Comprehension

result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)

# Method 2 (Best)
result_2 = [i for i in range(10) if i % 2 == 0]
print(result_2)