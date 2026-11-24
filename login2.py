username = "sojib"
password = "11223344"

luser = input("Enter Username:")
lpass = input("Enter Password:")

if username == luser:
    
    if password == lpass:
        print("login successfully")
    else:
        print("password not match")
    
    
else:
    print("username not match")
    