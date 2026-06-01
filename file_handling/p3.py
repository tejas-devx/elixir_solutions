#Write a Python program to append data to a file.

f = open("student.txt","a")
text = input("Enter text to append: ")
f.write(" " + text)
f.close()
f=open("student.txt","r")
data = f.read()
print(data)
f.close()
