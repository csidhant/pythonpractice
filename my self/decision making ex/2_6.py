age= int(input("what is your age:"))
license = input ("do you have a fishing license in MN (yes/no)? ")
parentlic =input("does your parent  have  a fishing license in MN (yes/no)?")
if (age < 16 and parentlic == "yes ") or license == "yes":
    print("you are legal to fish in Mn ")
else:
    print("you are not legal in fishing in MN")
    