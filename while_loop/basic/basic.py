#Print numbers from 1 to 10 using while loop.
i = 1

while i <= 10:
    print(i)
    i += 1

#Print even numbers up to 20.
i = 2

while i <= 20:
    print(i)
    i += 2

#Find sum of numbers from 1 to n.
n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)

#Print multiplication table.
n = int(input("Enter number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


#Reverse a number.
n = int(input("Enter number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number =", rev)