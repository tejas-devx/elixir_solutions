#Write a Python program to demonstrate Encapsulation using public and private variables.(Encapsulation)
class Student:

    def __init__(self):
        self.__mark = 90

    def show(self):
        print(self.__mark)

s = Student()

s.show()