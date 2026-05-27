#Write a function to find the area of a rectangle using length and breadth.

def rectangle(length,breadth):
    return length*breadth

l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
print(rectangle(l,b))