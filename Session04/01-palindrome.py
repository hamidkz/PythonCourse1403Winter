# پالیندروم رشته ای است که از هر دو طرف یک جور و یکسان خوانده می شود
# مثل Wow, nurses run, ...

text = input("Enter your string: ")
text = text.replace(' ', '').lower()
reversed_text = text[::-1]
print(text==reversed_text)


