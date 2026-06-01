#Write a Python program to check whether a number is even or odd usingexception handling.
try:
    num = int(input("Enter a number: "))

    if num%2==0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print("Please enter a valid number")
    