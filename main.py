operation = input('Please enter an operator (+, -, /, *): ')
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))

if operation == '+':
    results = num1 + num2
    print(f"The result is: {results}")
elif operation == '-':
    results = num1 - num2
    print(f"The result is: {results}")
elif operation == '/':
    if num2 != 0:
        results = num1 / num2
        print(f"The result is: {results}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '*':
    results = num1 * num2
    print(f"The result is: {results}")
else:
    print(f"Please enter a vaild operator {operation}")
