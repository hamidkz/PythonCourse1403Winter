dama = int(input("Enter dama:"))

# dama > 30 -> Garm
# dama < 10 -> Sard
# Motadel

if dama > 30:
    print("Garm")

if dama < 10:
    print("Sard")

if 10 <= dama <= 30:
    print("Motadel")


if dama > 30:
    print("Garm")
elif dama < 10:
    print("Sard")
else:
    print("Motadel")
