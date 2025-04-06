text = "Build and ship software on a single, collaborative platform"

# output = {
#     'a': 3,
#     'b': 4
# }

result = {} # ~ dict()
for char in text:
    result[char.lower()] = text.lower().count(char)

print(result)

