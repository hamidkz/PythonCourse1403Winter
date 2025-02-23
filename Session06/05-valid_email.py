email = input("Enter your email:")
# Valid email has @ and .

# Hamid.kz@gmail.com
# Hamid.kz@___________________.________

if '@' in email and '.' in email:
    atsign_pos = email.find("@")
    dot_pos = email.find('.', atsign_pos)
    if dot_pos > -1 != '.' :
        print("Your email is valid.")
    else:
        print("Sorry!")            
else:
    print("Sorry!")

