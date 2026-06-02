#Write a Python program to demonstrate Single Inheritance using classes Animal and Dog.(Single Inheritance)
class Animal:

    def show(self):
        print("I am an Animal")

class Dog(Animal):

    def bark(self):
        print("Dog Barking")

d = Dog()

d.show()
d.bark()