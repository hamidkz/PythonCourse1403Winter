
# 5 : 1, 2, 3, 4, 5 prime
# 4 : 1, 2, 3, 4 not prime

def is_prime(number):
    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
    return result


# number = int(input("Enter a number:"))
# print(is_prime(number))

for i in range(1,100):
    print(i, is_prime(i))




