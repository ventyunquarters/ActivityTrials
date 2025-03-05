def prog06():
    numbers = []
    for i in range(10):
        numbers.append(int(input(f"Enter number {i+1}: ")))
    result = numbers [0]
    for i in range (1,10):
        result -= numbers[i]
    print(result)
prog06()