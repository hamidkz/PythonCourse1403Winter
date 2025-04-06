
# a = 10

# def f():
#     # print(a)
#     global a
#     a = 20
#     # a: local variable
#     print(a)
    
# f()
# print(a)



def f():
    global a
    a = 10

def g():
    global a
    a = 20

a = 30
print('first:', a)
f()
print('after f called', a)
g()
print('after g called', a)