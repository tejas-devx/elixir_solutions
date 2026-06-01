#Write a Python program to read a file line by line.
f = open("student.txt", "r")

for line in f:
    print(line.strip())

f.close()