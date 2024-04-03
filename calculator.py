import math
import sys

# Defining the function for addition
def add(first_number, second_number):
    return first_number + second_number

# Defining the function for subtraction
def subtract(first_number, second_number):
    return first_number - second_number

# Defining the function for multiplication
def multiply(first_number, second_number):
    return first_number * second_number

# Defining the function for division, with error handling for division by zero
def divide(first_number, second_number):
    while True: # starts an infinite loop so it keeps asking the user for input, even after an error occurs
        try:
            result = first_number / second_number
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed, please change 2nd Number to a non-zero value")
            return None
    
# Defining the function for square root allowing only one number input, with error handling for negative inputs
def square_root(number):
    while True: # starts an infinite loop so it keeps asking the user for input, even after an error occurs
        try:
            return math.sqrt(number)
        except ValueError:
            print("Error: cannot take the square root of a negative number. ")
            return None
        
# Defining the function to get the numeric input from the user, with error handling for invalid inputs
def get_number(prompt): 
    while True: # starts an infinite loop so it keeps asking the user for input, even after an error occurs
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        

# Defining the main calculator function, that will loop or quit when 'x' is entered (only accepts 2 values, 1 for sqrt)
def calculator():
    while True: 
        operator = input("Enter an operator (+ - * / sqrt) or 'x' to quit: ")
        
        # Allows user to quit the program
        if operator == 'x':
            print("Ending program")
            sys.exit()

        # Get numbers from the user based on the operator selected
        if operator in ('+', '-', '*', '/'):
            first_number = get_number("Enter the 1st number: ")
            second_number = get_number("Enter the 2nd number: ")

        # Performing the operation depending on the operator selected
        if operator == "+":
            result = add(first_number, second_number)
        elif operator == "-":
            result = subtract(first_number, second_number)
        elif operator == "*":
            result = multiply(first_number, second_number)
        elif operator == "/":
            result = divide(first_number, second_number)
            if result is None:
                continue
        elif operator == 'sqrt':
            number = get_number("Enter the number for square root: ")
            result = square_root(number)
            if result is None:
                continue
        else:
            print(f"{operator} is not a valid operator")
            continue 
        
        # Displays the result of the calculation carried out to 3 decimal places 
            
        print(f"The result is: {round(result, 3)} ")
    
# Calling the function to run the calculator program
calculator()
