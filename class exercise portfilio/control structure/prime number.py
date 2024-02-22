#4. Write a program to print the prime numbers between 1 and 100.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

# Set the upper limit as 100
upper_limit = 100

# Print prime numbers between 1 and 100
print_primes(upper_limit)
