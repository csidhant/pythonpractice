x=float (input("enter 1st interger:"))
y= float (input("enter 2nd integer:"))
print("1)  add the two number" )
print("2)  subtract  the two number" )
print("3)   multiply the two number" )
print("4)  divide the two number" )
choice = int (input("please enter your choice:"))
print("the answer is :",end=" ")
if choice == 1:
    print(x+y)

elif choice ==2:
    print(x-y)
    
elif choice == 3:
    print(x*y)
        
elif choice ==4:
    print(x/y)
else:
     print("you did not enetr a valid choice :")
