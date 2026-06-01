#Write a program to create a login system with exception handling for invalid credentials.
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise ValueError("Invalid Credentials")

    print("Login Successful")

except ValueError as e:
    print(e)