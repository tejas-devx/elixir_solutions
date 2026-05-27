#Build a student management system (list + dict + loops)
students = {}

while True:

    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:

        name = input("Enter name: ")
        mark = int(input("Enter mark: "))

        students[name] = mark

    elif ch == 2:

        for k, v in students.items():
            print(k, ":", v)

    elif ch == 3:
        break