# Combined Program with Looping Menu
# Factorial and Fibonacci Calculator

# Function to calculate factorial
def factorial(n):
    result = 1  # initialize result

    for i in range(1, n + 1):
        result *= i  # multiply numbers

    return result


# Function to generate Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1  # first two terms

    for i in range(n):
        print(a, end=" ")  # print current term
        next_term = a + b  # compute next term
        a = b              # update values
        b = next_term
    print()  # move to next line


# Main program loop
while True:
    print("\n===== MENU =====")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            num = int(input("Enter a number: "))

            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {num} is {factorial(num)}")

        elif choice == 2:
            terms = int(input("Enter number of terms: "))

            if terms <= 0:
                print("Please enter a positive number.")
            else:
                print("Fibonacci sequence:")
                fibonacci(terms)

        elif choice == 3:
            print("Exiting program... Goodbye!")
            break  # exit loop

        else:
            print("Invalid choice. Please select between 1 and 3.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
