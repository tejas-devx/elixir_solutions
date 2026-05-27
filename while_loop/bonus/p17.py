#Create a shopping cart system
cart = []

while True:

    print("\n1.Add Item")
    print("2.View Cart")
    print("3.Remove Item")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:

        item = input("Enter item: ")
        cart.append(item)

    elif ch == 2:

        print("Cart Items:", cart)

    elif ch == 3:

        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)

    elif ch == 4:
        break