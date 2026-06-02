#Write a Python program to demonstrate Polymorphism using classes Dog and Cat with the same method sound().(Polymorphism)
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()