#Write a Python program to demonstrate Abstraction using an abstract class Shape and a subclass Square.(Abstraction)
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        side = 5
        print("Area =", side * side)

s = Square()

s.area()