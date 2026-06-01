#Write a program to remove an item from a list and handle exceptions.
try:
    l = [10, 20, 30, 40]

    item = int(input("Enter item to remove: "))

    l.remove(item)

    print(l)

except ValueError:
    print("Item not found in list")