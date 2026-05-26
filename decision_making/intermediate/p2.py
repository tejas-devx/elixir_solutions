#Find the largest of three numbers

n1 = int(input("Enter first number: "))
n2 = int(input("Enter two number: "))
n3 = int(input("Enter third number: "))

if n1>n2 and n1>n3:
    print(n1," is greater")
elif n2>n1 and n2>n3:
    print(n2," is greater")
elif n3>n1 and n3>n2:
    print(n3," is greater")
elif n1==n2:
    print(n1, n2," are same")
elif n1==n3:
    print(n1, n3," are same")
else:
    print(n2, n3, " are same")