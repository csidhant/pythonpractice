5# Write a program to find the factorial of a given number.
def factorial (n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)
user_input = input("enter a non negative integer:")
try:
    user_number = int(user_input)
    if user_number < 0:
        print("please enetr a non negative integer:")
    else:
        result= factorial (user_number)
        print(f"the factorial of {user_number} is: {result}")
except valueError:
    print("invalid input.please enetr a valid integer")
