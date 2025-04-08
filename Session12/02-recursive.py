
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1 = 4 * 3!

# fact(n) = n * fact(n-1)

number = 3
result = 1
for num in range(1, number + 1):
    result = result * num
print(result)

def fact(n):
    if n == 1:
        return 1
    else:
        # fact(n) = n * fact(n-1)
        result = n * fact(n-1)
        return result

# fact(3) => 3 * fact(2)
# fact(2) => 2 * fact(1)
# fact(1) => 1

print(fact(number))


