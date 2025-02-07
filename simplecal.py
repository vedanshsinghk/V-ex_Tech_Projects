def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

while True:
    print("\nSelect Operation")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {sub(num1, num2)}")
    elif choice == '3':
        print(f"Result: {mul(num1, num2)}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {div(num1, num2)}")
    else:
        print("INVALID INPUT, Please enter a valid choice.")
