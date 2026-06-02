#Write a Python program to create a BankAccount class with deposit andwithdrawal methods.(Class, Object, Methods)
class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Balance =", self.balance)

acc = BankAccount()

acc.deposit(5000)
acc.withdraw(1000)

acc.display()