'''5. Write a program to ask the user to input the numbers until they want.
The users can enter a positive or a negative numbers. The program should
calculate the sum of the positive numbers and the
negative numbers separately and display in a proper format.'''
'''def main():
    positive_sum = 0
    negative_sum = 0

    while True:
        user_input = input("Enter a number (or type 'stop' to finish): ")

        # Check if the user wants to stop
        if user_input.lower() == 'stop':
            break

        # Convert user input to a float
        try:
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Update sums based on the sign of the number
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number

    # Display the results
    print("\nSum of positive numbers: ", positive_sum)
    print("Sum of negative numbers: ", negative_sum)

if __name__ == "__main__":
    main()
'''
# without funtction
positive_sum = 0
negative_sum = 0

while True:
    user_input = input("Enter a number (or type 'stop' to finish): ")

    # Check if the user wants to stop
    if user_input.lower() == 'stop':
        break

    # Convert user input to a float
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Update sums based on the sign of the number
    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

# Display the results
print("\nSum of positive numbers: ", positive_sum)
print("Sum of negative numbers: ", negative_sum)
