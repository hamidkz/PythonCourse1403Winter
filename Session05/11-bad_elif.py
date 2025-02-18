
a = int(input())

# Bad 
if a % 2 == 0:
    print("Zoj")
elif a % 5 == 0:
    print("Mazrabe 5")
elif a % 10 == 0:
    print("Mazrabe 10")
else:
    print("Nemidoonam")


# Good
if a % 10 == 0:
    print("Mazrabe 10")
elif a % 5 == 0:
    print("Mazrabe 5")
elif a % 2 == 0:
    print("Zoj")
else:
    print("Nemidoonam")