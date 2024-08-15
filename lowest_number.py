# Define the range
start = 20
end = 30

# List of even numbers
even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]

# List of odd numbers
odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
#
for num in range(50, 4, -1):
    print(num)
#
for i in range (100000):
print(i)
#calculater
def perform_calculation():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")

def main():
    while True:
        perform_calculation()
        
        # Ask user if they want to continue
        user_input = input("Do you want to perform another calculation? (y/n): ").lower()
        if user_input != 'y':
            print("Terminating the c


