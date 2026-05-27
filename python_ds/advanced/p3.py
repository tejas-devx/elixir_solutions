#Implement a stack using a list.
stack = []

while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        item = input("Enter item: ")
        stack.append(item)

    elif ch == 2:
        if len(stack) == 0:
            print("Stack Empty")
        else:
            print("Popped:", stack.pop())

    elif ch == 3:
        print(stack)

    elif ch == 4:
        break