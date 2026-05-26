#ATM withdrawal condition (balance check)
balance = int(input("Enter balance: "))
amount = int(input("ENter amount to withdraw"))

if amount <=balance:
    if amount % 100 == 0:
        print("Withdrawal successfull")
    else:
        print("Enter amount as multiples of 100")
else:
    print("Insufficient balance")