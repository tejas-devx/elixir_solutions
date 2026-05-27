#Keep taking input until user enters "exit".
while True:

    s = input("Enter something: ")

    if s.lower() == "exit":
        break

    print("You entered:", s)