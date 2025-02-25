text = input("Enter your text:")

# text = "hamid"

original = "abcdefghijml1234567890"
mapping =  "poiuytrewasdfghjkl,vcT"

result = ""
for ch in text:
    ch_pos = original.find(ch)
    result = result + mapping[ch_pos]
print(text)
print(result)