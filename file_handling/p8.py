#Write a Python program demonstrating seek().
f = open("student.txt", "r")

f.read(5)

f.seek(0)

print(f.read(5))

f.close()