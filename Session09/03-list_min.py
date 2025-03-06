lst = [-2.3 ,98, -1, 12, 5]
# output: 98 max

result = lst[0]
for num in lst:
    if num > result:
        result = num
print(result)

result_2 = max(lst)
print(result_2)
