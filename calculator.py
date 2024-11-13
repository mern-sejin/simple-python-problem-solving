# PROBLEM-2: simple functional calculator
input1 = int(input('Input-1: '))
input2 = int(input('Input-2: '))
operator = input('Operator (+, -, *, /, %): ')
result = 0

def add (num1, num2):
    return num1 + num2
def substract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return int(num1 / num2)
def modulo (num1, num2):
    return num1 % num2

if operator == '+':
    result = add(input1, input2)
elif operator == '-':
    result = substract(input1, input2)
elif operator == '*':
    result = multiply(input1, input2)
elif operator == '/':
    result = divide(input1, input2)
elif operator == '%':
    result = modulo(input1, input2)
else:
    print('Invalid Operator!')
print('Result: ', result)