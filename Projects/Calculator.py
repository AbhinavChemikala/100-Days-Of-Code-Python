logo = """ _____________________
|  _________________  |
| | Abhinav      0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

# Addition
def add(n1,n2):
    return n1+n2

# Subtraction
def subtract(n1,n2):
    return n1-n2

# Multiplication
def multiply(n1,n2):
    return n1*n2

# Division
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator(): 
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol) 
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation from the above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2) 
        print(f"{num1} {operations_symbol} {num2} = {answer}") 
        if input(f"Type 'y' to continue calculate with {answer} or 'n' to start new: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()