print('Welcome to Python calculator!!')

num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
op = input('Enter a operand ')

if op == '+':
    print('Addition is: ', num1+num2)

elif op == '-':
    print('Subtraction is: ', num1-num2)

elif op == '*':
    print('Multiplication is: ', num1*num2)

elif op == '/':
    print('Divison is: ', num1//num2)

else:
    print('Invalid Operator')