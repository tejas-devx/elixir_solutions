#Write a Python program to demonstrate Multiple Inheritance using classes Father,Mother, and Child.(Multiple Inheritance)
class Father:

    def driving(self):
        print("Driving Skill")

class Mother:

    def cooking(self):
        print("Cooking Skill")

class Child(Father, Mother):

    def playing(self):
        print("Playing Football")

c = Child()

c.driving()
c.cooking()
c.playing()