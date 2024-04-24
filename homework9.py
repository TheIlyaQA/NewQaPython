n = int(input("Enter n: "))

if 1 <= n <= 9:
    for i in range(1, n + 1):
        print(" " * (2 * (n - i)), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
else:
    print("n number is out of range. Please enter a number between 1 and 9")
