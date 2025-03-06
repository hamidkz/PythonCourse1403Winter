# k = 12
# 1 * 12 = 12
# 2 * 6 =12
# 3 * 4 = 12
# 4 * 3  = 12
# 6 * 2=12
# 12 * 1 = 12

num = 12
for i in range(num+1):
    for j in range(num+1):
        if i * j == num: #12 *12 = 144
            print(i, j)

# Better solution
for i in range(1, num+1): # 3
    if num % i == 0: # 12 % 3 = 0 
        print(i, int(num / i))
