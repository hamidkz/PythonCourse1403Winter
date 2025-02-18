# babak -> 1abak (Replace b with 1 in "first" position)

text = 'abbas'
first_b_index = text.find('b') #  first_b_index = 1

result = text[:first_b_index] + '1' + text[first_b_index+1:]
print(result)

# Method 2
print(text.replace("b", "1", 1))


