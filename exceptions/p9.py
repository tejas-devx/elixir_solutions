#Write a Python program to handle multiple exceptions in a banking application.
try:
    balance = 10000

    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance")

    print("Remaining Balance =", balance - amount)

except ValueError as e:
    print(e)

except Exception:
    print("Something went wrong")