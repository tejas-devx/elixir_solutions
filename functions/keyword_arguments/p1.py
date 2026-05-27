#Create a function employee(name, salary) and call it using keyword arguments.

def employee(name,salary):
    print("Employee: ",name)
    print("Salary: ",salary)

name = input("Enter the name: ")
salary = int(input("Enter salary: "))
employee(name=name,salary=salary)