#Implement a queue using a list.
queue = []

while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        item = input("Enter item: ")
        queue.append(item)

    elif ch == 2:
        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Removed:", queue.pop(0))

    elif ch == 3:
        print(queue)

    elif ch == 4:
        break