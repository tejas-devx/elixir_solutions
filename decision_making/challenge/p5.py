#Check if a number lies between two numbers

num = int(input("Enter number: "))
a = int(input("Enter first limit: "))
b = int(input("Enter second limit: "))

if a < num < b:
    print("Number lies between")
else:
    print("Number does not lie between")