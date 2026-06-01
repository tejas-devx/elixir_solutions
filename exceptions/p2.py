#Write a program to calculate the average of 3 numbers and handle invalidinput.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    avg = (a+b+c)/3

    print("Average = ",avg)

except ValueError:
    print("Invalid Input")