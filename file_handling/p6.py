#Write a Python program using writelines().
f = open("student.txt", "w")

names = [
    "Tejas\n",
    "Rahul\n",
    "Anu\n"
]

f.writelines(names)

f.close()

print("Written Successfully")