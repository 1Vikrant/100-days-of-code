#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for keys in operations:
        print(keys)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        x = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation, or enter 'e' to end calculation: ")

        if x == "y":
            num1 = answer
        elif x == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()