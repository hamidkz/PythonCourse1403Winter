# Syntax Error
# prnt('hamid')
# print "hamid"

# Runtime Error
# a = 1 / 0

# Logical Error, Semantic Error

# def fun(x,y):
#     return x*y

# print(fun(2,3))

# print(fun(2, 3) == 5)


a = input('Enter a:')
b = input('Enter b:')

# exception

try:
    result = int(a) / int(b)
    print(result)
except ZeroDivisionError:
    print("b نباید صفر باشد")
except ValueError:
    print("Har do bayad int bashanad")






