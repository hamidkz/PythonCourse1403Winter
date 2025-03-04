text_1 = "hamed"
text_2 = "ahmad"

# result = "haid" # حروف مشترک

result_1 = ''
# Method 1: Good
for char_1 in text_1:
    if text_2.find(char_1) > -1:
        result_1 += char_1
print(result_1)

result_2 = ''
for char_1 in text_1:
    for char_2 in text_2:
        if char_1 == char_2 and char_2 not in result_2:
            result_2 += char_1
print(result_2)
