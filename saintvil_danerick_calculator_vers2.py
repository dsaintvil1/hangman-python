"""
Danerick Saint-Vil
November 6, 2025
Homework 02
Terminal Calculator
"""

print("Please enter an Expression\n")

# Functions for all operations
def addition(left, right):

    return left + right

def subtraction(left, right):

    return left - right

def multiplication(left, right):

    return left * right

def division(left,right):

    try: # Tries to divide
        return left / right
    except ZeroDivisionError: # Can't divide by zero
        return ("Can't divide by zero")

def modulo(left, right):

    try: # Tries to divide
        return left % right
    except ZeroDivisionError: # Can't divide by zero
        return ("Can't divide by zero")

def power(left, right):

    return left ** right

def floor(left, right):

    try: # Tries to divide
        return left // right
    except ZeroDivisionError: # Can't divide by zero
        return ("Can't divide by zero")


def calculate(equation): # Function for calculating expression
    equation = equation.split() # Splits the string into a list

    

    # If there are more than two numbers, or the operations don't match, return error
    if len(equation) != 3 or equation[1] not in ["+", "-", "*", "/", "%", "**", "//"]:
        return (f"Error: Invalid Expression - ({" ".join(equation)})")
    else:
        print(f"Result: {" ".join(equation)} = ", end="")
        # Both of these if statements check for a "."
        # If there is, converts the two ends into a float; else, integer
        try:
            if "." in equation[0]: 
                equation[0] = float(equation[0])
            else:
                equation[0] = int(equation[0])

            if "." in equation[2]:
                equation[2] = float(equation[2])
            else:
                equation[2] = int(equation[2])
        except ValueError:
            return ("Invalid number input")

        
    # Now check the middle of the list for the operation, and use the functions that are listed above
        if equation[1] == "+":
            return addition(equation[0], equation[2])
        elif equation[1] == "-":
            return subtraction(equation[0], equation[2])
        elif equation[1] == "*":
            return multiplication(equation[0], equation[2])
        elif equation[1] == "/":
            return division(equation[0], equation[2])
        elif equation[1] == "%":
            return modulo(equation[0], equation[2])
        elif equation[1] == "**":
            return power(equation[0], equation[2])
        elif equation[1] == "//":
            return floor(equation[0], equation[2])

def main():
    expression = input(":> ") # Gets the input
    while expression not in ["quit", "q"]: # If quit or q is the input, end the loop
        print(f"{calculate(expression)}") # Prints whatever the function returns
        expression = input(":> ")

main()