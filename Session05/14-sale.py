# 5XXX -> VIP

code = input("Enter your code:")
factor_val = int(input("Enter your factor value:"))

if code.startswith("5"): # VIP
    if factor_val > 1000000:
        price = 80 * factor_val / 100
    else:
        price = 90 * factor_val / 100
else:
    if factor_val > 1000000:
        price = 95 * factor_val / 100
    else:
        price = factor_val

print(price)