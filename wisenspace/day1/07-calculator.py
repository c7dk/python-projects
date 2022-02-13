def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2
    
def main():
    print('The operations you can do are add, subtract, multiply, divide and modulo. (You have to spell the operations exactly or the calculator will not work.)')
    operation = input('Please enter the operation you want to do: ')
    print(operation)
    in1 = input('Please enter your first number: ')
    in2 = input('Please enter your second number: ')

    in1 = int(in1)
    in2 = int(in2)

    if(operation == 'add'):
        answer = add(in1, in2)
    elif(operation == 'subtract'):
        answer = subtract(in1, in2)
    elif(operation == 'multiply'):
        answer = multiply(in1, in2)
    elif(operation == 'divide'):
        answer = divide(in1, in2)
    elif(operation == 'modulo'):
        answer = modulo(in1, in2)

    print(f"operation>>> {in1} {operation} {in2} = {answer}")

main()