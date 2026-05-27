#ATM simulation (withdraw, deposit, check balance).
balance = 10000

while True:

    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Deposited Successfully")

    elif ch == 2:
        amt = int(input("Enter amount: "))

        if amt <= balance:
            balance -= amt
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    elif ch == 3:
        print("Balance =", balance)

    elif ch == 4:
        break

    else:
        print("Invalid Choice")