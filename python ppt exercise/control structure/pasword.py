#WAP to force user to re-enter the name and password until name equals to saurav and password
#equals 12345 is entered.
valid_name = "sidhant"
valid_password= "12345"
while True:
    name= input("enter the name of user:")
    password = input("enetr the password:")
    if name == valid_name and  password == valid_password:
        print("welcome ",valid_name)
        break
    else:
        print("sorry! the name you are using is incorrect")


