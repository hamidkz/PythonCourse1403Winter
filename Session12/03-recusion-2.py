lst = [9, -1, 100, 7]

# Method 1
print(min(lst))

# Method 2
pass

# Method 3
# get_min([9, -1, 100, 7]) = min(9, get_min([-1, 100, 7]))
# get_min([7]) = 7

def get_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], get_min(lst[1:]))

print(get_min([9, -1, 100, 7]))
