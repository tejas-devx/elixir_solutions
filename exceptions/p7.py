#Write a Python program to handle errors while converting string to float.
try:
    num = float(input("Enter value: "))

    print("Float value =", num)

except ValueError:
    print("Invalid float value")