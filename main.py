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




# Exercise 2 Below

weight = float(input('Please enter your weight below: '))
unit = input('Please enter the unit of weight Kilograms or Pounds (K or P): ').strip().upper()

if unit == 'K':
    weight *= 2.05
    unit = 'Pounds'
elif unit == 'P':
    weight /= 2.05
    unit = 'Kilograms'
else:
    print("Please enter a correct unit.")
    exit()  # Exit the program if the input is invalid

print(f"You are {round(weight, 1)} {unit}")
