from random import randint

i = 0
ghabli = -1
while True:
    i += 1
    number = randint(0,1)
    print(i, number)
    if ghabli == number == 0:
        break
    else:
        ghabli = number

    