#Check triangle type (equilateral, isosceles, scalene)
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a==b:
    if b==c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")
        