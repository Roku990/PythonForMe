import math

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Cannot divide with zero"
    return x/y

def power(x,y):
    return x ** y

def modulus(x,y):
    return x%y

def squareRoot(x):
    if x<0:
        return "Cannot get the root of a negative number"
    return math.sqrt(x)

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Goodbye!")
            break

        try:
            if choice == '7':
                num = float(input("Enter Number:"))
                print(f"The result {squareRoot(num)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {add(num1,num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1,num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1,num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1,num2)}")
                elif choice == '5':
                    print(f"Result: {power(num1,num2)}")
                elif choice == '6':
                    print(f"Result: {modulus(num1,num2)}")
                else:
                    print("Invalid Choice. Try Again.")
        except ValueError:
            print("Please enter a valid number")


calculator()