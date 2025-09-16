"""Console Bassed"""
import os


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

result = None

while 1:
    if result == None:
        num1 = float(input('What is the first number? : '))
    else:
        num1 = result

    for symbol in operations:
        print(symbol)
    
    operation_symbol = input('Pick an operation from the line  above: ')
    num2 = float(input('What is the second number? : '))

    calculation_function = operations[operation_symbol]

    result = calculation_function(num1, num2)

    print(f'{num1}{operation_symbol}{num2} = {result}')

    continue_or_not = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to exit.: ')
    if continue_or_not == 'n':
        os.system('cls')
        result = None
    else:
        os.system('cls')
        continue


