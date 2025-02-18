orginal_username = 'hamidkz'
orginal_password = '1234'

username = input("Username")
if username == orginal_username:
    password = input("Password")
    if password == orginal_password:
        print("OK")
    else:
        print("Password Error")
else:
    print("Username Error")
