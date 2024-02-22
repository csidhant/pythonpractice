s= input("please enter a list of integer:")
lst= s.split() # here lst is list of string
# make a guess first
containsEven = False
# the iterate over the list
for element in lst :
    x = int (element)
   # check your guess in the loop and fix it if you need
    if x %2 ==0:
       containsEven = True
       # after the loop you know whether your guess was correct or not
if containsEven:
    print("the list contains the even number")
else:
    print ("the list didnt contains even number")
     
