text = 'Iran'
count_a = text.count('a') # 1
find_a = text.find('a') # 2
find_T = text.find('T') # -1
index_a = text.index('a') # 2 == text.find('a')
index_T = text.index('T') # Error خطا به خاطر اینکه حرف تی را پیدا نمیکند

check_alpha = "a".isalpha() # True
check_numeric_a = "a".isdigit() # False
check_numeric_10 = "10".isdigit() # True
check_numeric_10 = "10".isdecimal() # True == "10".isdigit()
check_alphabetic_or_numeric = "iran22".isalnum() # True
check_alphabetic_or_numeric_2 = "iran22@".isalnum() # False


