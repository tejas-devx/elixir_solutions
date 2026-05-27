#Validate input until correct value is given.
password = "admin123"

while True:

    p = input("Enter password: ")

    if p == password:
        print("Access Granted")
        break

    else:
        print("Wrong Password")