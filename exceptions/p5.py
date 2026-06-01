#Write a Python program to handle password validation using custom exceptions.
try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")

    print("Valid Password")

except ValueError as e:
    print(e)