n = int(input("Input panjang element: "))
for i in range(1, n + 1, 1):
    if n <= i:
        print(i, end='')
    else:
        print(i, end='')
        print("+", end='')
