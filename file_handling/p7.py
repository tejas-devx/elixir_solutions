#Write a Python program demonstrating tell().
f = open("student.txt", "r")

print("Current Position:", f.tell())

f.read(2)

print("Position After Reading:", f.tell())

f.close()