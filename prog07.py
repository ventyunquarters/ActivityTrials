def prog07():
    numbers = []
    for i in range(10):
        numbers.append(int(input(f"Enter number {i+1}: ")))
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    print(even_count)
prog07()