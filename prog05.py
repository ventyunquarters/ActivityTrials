def prog05():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 % num2)
prog05()