age = int(input("please enter your age:"))
resident = input("are you natural born citizen of Nepal: ")
years= int(input("how much it must be to be a ctizen of nepal: "))
eligible= True
if age <35:
    eligible=False
if resident != "yes":
    eligible=False
if years <14:
    eligible=False
if eligible:
    print("you can fight for election")
else:
    print("sorry you are not able to fight for election")