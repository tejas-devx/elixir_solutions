#Write a program to read numbers from a file and handle possible exceptions.
try:
    file = open("numbers.txt", "r")

    data = file.read()

    print(data)

    file.close()

except FileNotFoundError:
    print("File not found")