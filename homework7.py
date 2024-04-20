triangle = int(input("Enter size of triangle: "))
symbol = "*"

for i in range(triangle):
    for j in range(triangle - i - 1):
        print(" ", end='')
    for k in range(i + 1):
        print(symbol, end='')
    print()
