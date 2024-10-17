def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter a operation (+,-,*,/): ")


if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":     
    result = (num1 - num2)
    print(result)
elif operation == "*":
    result =(num1 * num2)
    print(result)
elif operation == "/":
    result = num1 / num2
    print(result)
else:
    print("error")