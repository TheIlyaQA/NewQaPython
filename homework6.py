height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
symbol = "^"

for i in range(height):
    for j in range(width):
        print(symbol, end='')
    print()