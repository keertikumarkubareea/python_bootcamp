"""
Calculator capstone project
Operations: add, subtract, multiply, divide

"""
logo = """
 _____________________
|  _________________  |
| | KubCalculus  0. | |  
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
|_____________________|
"""


def add(n1: float, n2: float) -> float:
    return n1 + n2


def sub(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    if n2 == 0:
        print("Division by 0 is not allowed")
        return 0
    else:
        return n1 / n2


def calculate(op: str, op1: float, op2: float) -> float:
    if op == "+":
        result = add(n1=op1, n2=op2)
    elif op == "-":
        result = sub(n1=op1, n2=op2)
    elif op == "/":
        result = divide(n1=op1, n2=op2)
    else:
        result = multiply(n1=op1, n2=op2)
    return result


def new_calc() -> float:
    operation = input("Please choose an operation: +, -, /, *: ")
    while operation != "+" and operation != "-" and operation != "/" and operation != "*":
        operation = input("Please enter a valid operation: +, -, / or *: ")
    operand1 = float(input("Please enter the first number: "))
    operand2 = float(input("Please enter the second number: "))
    result = calculate(op=operation, op1=operand1, op2=operand2)
    print(f"The result of {operand1} {operation} {operand2} = {result}")
    return result


def follow_up_calc(result: float) -> float:
    operand1 = result
    operation = input(f"Please enter an operation for operand {operand1} -> +, -, /, *: ")
    while operation != "+" and operation != "-" and operation != "/" and operation != "*":
        operation = input("Please enter a valid operation: +, -, / or *: ")
    operand2 = float(input("Please enter the second number: "))
    result = calculate(op=operation, op1=operand1, op2=operand2)
    print(f"The result of {operand1} {operation} {operand2} = {result}")
    return result


def main():
    print(logo)
    calc_done = False
    result_calc = new_calc()
    while not calc_done:
        proceed = input(
            f"Enter 'stop' to end the process, 'continue' to use {result_calc} in the next calculation"
            f"\nor 'new' to start a new calculation: ")
        while proceed != "stop" and proceed != "new" and proceed != "continue":
            proceed = input("Please enter a valid way to proceed: 'stop', 'continue' or 'new': ")
        if proceed == "stop":
            calc_done = True
        elif proceed == "continue":
            result_calc = follow_up_calc(result_calc)
        else:
            result_calc = new_calc()


if __name__ == "__main__":
    main()
