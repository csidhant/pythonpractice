# 2. Write a program to check whether a user input number is prime or not.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
user_input = input("Enter a number: ")

# Validate user input
try:
    user_number = int(user_input)
    if user_number < 0:
        print("Please enter a positive integer.")
    else:
        if is_prime(user_number):
            print(f"{user_number} is a prime number.")
        else:
            print(f"{user_number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
    
'''
i = 2
prime = True
for i in range(10):
    if i == num:
        continue
    
    if num % i == 0:
        prime = False
        break

if prime == True:
    print('Prime')
else:
    print('Not prime')
'''
