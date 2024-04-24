a = float(input("Enter number1: "))
b = float(input("Enter number2: "))
c = float(input("Enter number3: "))

if a == b == c:
    print("All three numbers are equal.")
else:
    max_number = None

    if a >= b and a >= c:
        max_number = a
    elif b >= a and b >= c:
        max_number = b
    else:
        max_number = c

    print(f"The maximum number of 3 user-entered numbers is: {max_number}")
