#Write a Python program to create a file and write data into it.
f = open("student.txt","w")

name = input("Enter text: ")
f.write(name)
f.close()
print("Data written successfully")