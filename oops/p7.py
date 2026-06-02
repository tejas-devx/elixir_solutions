#Write a Python program to demonstrate Method Overriding using parent and child classes.(Runtime Polymorphism)
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barking")

d = Dog()

d.sound()