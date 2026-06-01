#Write a Python program to read a file.
f =open("student.txt","r")
data = f.read()
print(data)
f.close()
