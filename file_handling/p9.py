#Write a Python program to create a file using exclusive mode.
try:
    f = open("newfile.txt", "x")

    f.write("File Created")

    f.close()

    print("File Created Successfully")

except FileExistsError:
    print("File Already Exists")