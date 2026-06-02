#Write a Python program to create a class Student and display student details using an object.(Class and Object)
class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)

name = input("Enter Name: ")
course = input("Enter Course: ")

s = Student(name, course)

s.display()
