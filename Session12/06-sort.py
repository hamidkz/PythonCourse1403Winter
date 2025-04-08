my_list = [3, -1, 10, -4]
# [-1, 3, -4, 10]

def sort_function(x: int):
    return x ** 2

my_list.sort(key=sort_function)
print(my_list)
