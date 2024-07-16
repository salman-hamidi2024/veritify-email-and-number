def check_phonenumber(x):
    global status
    if len(x) == 11 and x.startswith("09"):
        print(True)
        status = True
    elif len(x) == 13 and x.startswith("+989"):
        print(True)
        status = True
    elif len(x) == 14 and x.startswith("00989"):
        print(True)
        
        status = True
    else:
        print("it's not avilable please try again!")
        status = False
        print(status)
        

def check_emailaddress(x):
    global status
    if x in " ":
        print("you can't use space in email")
        status = False
    elif "@" not in x:
        print("your email shoud have @" )
        status = False
    elif not x.endswith(".com"):
        print("email should end with {.com}")
        status = False
    else:
        print("youre email checked it's safe")
        status = True



while True:
    user_phone = input("enter number: ")
    check_phonenumber(user_phone)
    if status == True:
        print("succefull your number is safe")
        break
    else:
        continue
while True:
    
    email = input("enter your email address: ")
    check_emailaddress(email)
    if status == True:
        print("your account made!")
        break
    else:
        continue
    
