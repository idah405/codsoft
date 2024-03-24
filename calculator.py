def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

Select_operation = input("please choose one operation (+, -, *, /): ")
First_num = float(input("Please enter the first number: "))
second_num = float(input("Please enter the second number: "))
if Select_operation == "+":
    print(f"{First_num} + {second_num} = The answer is {add(First_num, second_num)}")
elif Select_operation == "-":
            print(f"{First_num} - {second_num} = {subtract(First_num, second_num)}")
elif Select_operation == "*":
            print(f"{First_num} * {second_num} = {multiply(First_num, second_num)}")
elif Select_operation == "/":
            print(f"{First_num} / {second_num} = {divide(First_num, second_num)}")
else:
            print("Intput operation is Invalid. Be sure to choose from (+, -, *, /)")