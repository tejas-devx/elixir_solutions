#Write a Python program using a constructor (__init__) to initialize anddisplay employee details.(Constructor)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

name = input("Enter Name: ")
salary = int(input("Enter Salary: "))

e = Employee(name, salary)

e.display()