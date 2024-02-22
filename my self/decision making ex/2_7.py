try:
    age= int(input("what is your age:"))
except: 
    print ("you  did not enter your age correctly:")
    exit(0)
license= input("do you have a license")
parentlic= input("do your parent have license:")
if (age <16 and parentlic=="yes") or license=="yes":
    print("you are legel to drive:")
else:
    print("sorry!! you cant drive")