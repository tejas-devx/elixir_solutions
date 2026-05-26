#Simple calculator (based on operator +, -, *, /)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
opr = input("Enter the operator: ")

if opr =="+":
    print(n1+n2)
elif opr =="-":
    print(n1-n2)
elif opr == "*":
    print(n1*n2)
elif opr == "/":
    print(n1/n2)
else:
    print("Invalid operator")