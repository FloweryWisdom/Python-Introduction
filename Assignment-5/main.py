#Create caclulator functions. 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x/y

def exponent(x, y):
    return x ** y

def get_operation_choice():
    print("Please select an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    while True:
        try:
            choice = int(input("Enter choice (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                print(("Invalid choice. Please enter a number between 1 and 5."))
        except ValueError:
            print("Invalid choice. Please enter a valid number choice.")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter a valid number")

def calculator(): 
    choice = get_operation_choice()
    num1, num2 = get_numbers()

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    elif choice == 5:
        print("Result:", exponent(num1, num2))

calculator()
    
