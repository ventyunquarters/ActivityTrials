def prog10():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 < num2:
        start = num1 + 1
        end = num2
    else:
        start = num2 + 1
        end = num1
    for num in range(start, end):
        print(num)

prog10()