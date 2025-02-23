
text = "hamid"

# اگر حرف اول صدادار بود یا فقط یک کلمه داشتیم، عبارت را کپیتالایز کن

if text[0] in "aeiou" or text.count(" ") == 0:
    result = text.capitalize()
else:
    result = text
print(result)
