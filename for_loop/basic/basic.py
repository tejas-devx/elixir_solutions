#Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#Print even numbers between 1 to 50.
for i in range(2,51,2):
    print(i)

#Find sum of numbers from 1 to n.
n = int(input("Enter n: "))
total = 0

for i in range(1,n+1):
    total +=i

print("Sum= ",total)

#Print multiplication table of a number.
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#Iterate through a list and print each element.
l = input("Enter elements: ").split()

for i in l:
    print(i)