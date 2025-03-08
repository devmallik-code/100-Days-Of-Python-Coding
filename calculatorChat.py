def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Error: Division by zero"

operations_symbols = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    n1 = float(input("Enter first number: "))
    operation = input("Enter operation (+,-,*,/): ")
    n2 = float(input("Enter second number: "))

    if operation in operations_symbols:
        answer = operations_symbols[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")
    else:
        print("Invalid operation! Please enter one of (+, -, *, /)")
        continue  # Restart the loop if invalid input is given

    while True:
        continues = input("Work with previous result (y) or start new calculation (n)? ").lower()

        if continues == 'y':
            operation = input("Enter operation (+,-,*,/): ")
            n2 = float(input("Enter second number: "))

            if operation in operations_symbols:
                n1 = answer
                answer = operations_symbols[operation](answer, n2)
                print(f"{n1} {operation} {n2} = {answer}")
            else:
                print("Invalid operation! Please enter one of (+, -, *, /)")
        
        elif continues == 'n':
            break  # Exit inner loop and start a new calculation
        
        else:
            print("Invalid choice! Enter 'y' or 'n'.")
