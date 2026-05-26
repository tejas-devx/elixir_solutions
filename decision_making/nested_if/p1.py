#Find largest of three numbers using nested if
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

if n1>n2:
    if n1>n3:
        print(n1," is largest")
    else:
        print(n3," is largest")
else:
    if n2>n3:
        print(n2," is largest")
    else:
        print(n3," is largest")