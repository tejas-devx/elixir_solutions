#Write a Python program to demonstrate Multilevel Inheritance using classes A,B, and C.(Multilevel Inheritance)
class A:

    def methodA(self):
        print("Class A")

class B(A):

    def methodB(self):
        print("Class B")

class C(B):

    def methodC(self):
        print("Class C")

obj = C()

obj.methodA()
obj.methodB()
obj.methodC()