# List Comprehension
# my_list = [1, 2, 3]
# my_list = [ 1 == 1, isinstance(1.2, int)]
# print(my_list)

# output: [(0,0) , (1,1), (2,2)]

result = []
for i in range(3):
    result.append((i,i))
print(result)

# Method 2 (Best)
result_2 = [(i, i) for i in range(3)]
print(result_2)