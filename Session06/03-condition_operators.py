a = 10
b  = -20

if a > 0:
    if b > 0:
        print("a,b > 0")
    else:
        print("a > 0 ,b < 0")
else:
    if b > 0:
        print("a < 0 , b > 0")
    else:
        print("a < 0 , b < 0")

if a > 0 and b > 0: 
    print("a, b > 0")
elif a > 0 and b < 0:
    print("a > 0 , b < 0")
elif a < 0 and b > 0:
    print("a < 0 , b > 0")
elif a < 0 and b < 0:
    print("a, b < 0")

if a >0 and b < 10:
    pass
else:
    pass
