age = int (input("enter your age:"))
member = True
if age <= 15:
    member = False
if age >= 18:
    member = False
if member:
    print("you can join")
else:
    print("you can't join")
    
