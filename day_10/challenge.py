# Calculator
result = 0
continue_calc = True

def addition(first_number, second_number):
    return (first_number + second_number)

def subtraction(first_number, second_number):
    return (first_number - second_number)

def multiplication(first_number, second_number):
    return (first_number * second_number)

def division(first_number, second_number):
    return (first_number / second_number)

dict_calculator = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def show_operators():
    print("""
    +
    -
    *
    /      
    """)

def getParamsToCalculator(result): 
    if(result == 0): 
        first_number = float(input("What's the first number?"))
    else:
        first_number = result
        
    show_operators()
    operation = ""
    while (not operation in ["+", "-", "*", "/"]):
        operation = input('Pick an operation: ')

    second_number = float(input("What's the next number?"))
    
    return {
        "first_number": first_number,
        "operation": operation,
        "second_number": second_number
    }


result = 0
while continue_calc == True:
    dict_params = getParamsToCalculator(result)
    result = dict_calculator[dict_params['operation']](dict_params['first_number'], dict_params['second_number'])
    print(f"{dict_params['first_number']} {dict_params['operation']} {dict_params['second_number']} = {result} ")
    decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    
    if(not decision == 'y'):
        result = 0
