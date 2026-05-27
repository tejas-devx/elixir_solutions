#Menu-driven program using while loop.
while True:

    print("\n1.Add")
    print("2.Subtract")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif ch == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference =", a - b)

    elif ch == 3:
        break

    else:
        print("Invalid Choice")