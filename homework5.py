a = float(input("Enter number1: "))
b = float(input("Enter number2: "))
c = float(input("Enter number3: "))

if a > b and a > c:
    print(f"The maximum number of 3 user-entered numbers is: {a}")
if b > a and b > c:
    print(f"The maximum number of 3 user-entered numbers is: {b}")
if c > a and c > b:
    print(f"The maximum number of 3 user-entered numbers is: {c}")
