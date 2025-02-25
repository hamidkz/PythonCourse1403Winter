num = "654393954" # min:6 min: 5 min:4 min:3 .. 
# output: 3

min = int(num[0]) 
for n in num:
    if int(n) < min:
        min = int(n)
print(min)

