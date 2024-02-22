try:
    top =int (input("enter a numenator:"))
    
except valueError:
    print("you didnt enter a integer")
    exit(0)
try:
    bottom= int (input("enter a denomenator:"))
except:
    print("you didnt enter an integer")
    exit(0)
try:
    if top%bottom == 0:
        print("the numenator is evenly divided by the " + "denomenator.")
    else:
        print("the function is not whole number")
except zerDivisionError:
    print("the denomenator cannot be zero")
