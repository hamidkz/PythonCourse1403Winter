# def get_sum(x,y,z=0):
#     return x+y+z

# result = get_sum(2,3)
# print(result)


def get_sum(*args):
    return sum(args)

print(get_sum(1,2,3, 10, 300, -1))
print(get_sum())

