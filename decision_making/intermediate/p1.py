#Find the (greater) of two numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1>n2:
    print(n1," is greater")
elif n2>n1:
    print(n2," is greater")
else:
    print("same")