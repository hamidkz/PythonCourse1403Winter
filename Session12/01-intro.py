# [1, 10, 2]

# d = {
#     "name": "Ali",
#     "age": 26,
#     "father_name": "Hasan"
# }

x = 1000

def my_function(z):
    global x
    x = 1
    y = 2
    # print(x+y+z)
    return x+y+z

my_function(10)
print(x)

# print(my_function(10))
# t = my_function(500)
# print(t*2)