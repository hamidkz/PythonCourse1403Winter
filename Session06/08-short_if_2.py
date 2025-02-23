score = 13

if score < 10:
    result = "مردود"
elif score < 12:
    result = "مشروط"
else:
    result = 'قبول'

print(result)

result_2 = "مردود" if score < 10 else "مشروط" if score < 12 else "قبول"
print(result_2)