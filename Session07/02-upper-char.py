text = "Welcome to Iran"

for ch in text:
    if ch.isalpha() and ch.upper() == ch:
        print(ch, text.find(ch))
print("Done.")
