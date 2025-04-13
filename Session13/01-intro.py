def my_func(*args, **kwargs):
    print('args:', args)
    print('kwargs', kwargs)

# my_func("hamid", 10)
# my_func(300, name='hamid', age=10, father_name='ali')

# 10, 3 => 10 / 3 => 3, 1
def function_1(x, y):
    d = 10 // 3
    r = 10 % 3
    # return d, r
    return {
        'kharej': d,
        'baghimandeh': r
    }

# print(function_1(10, 3))


l = [1,2,3]
for index, item in enumerate(l):
    print(index, item)
