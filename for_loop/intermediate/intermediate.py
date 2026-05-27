#Count vowels in a string.
s = input("Enter string: ")

count = 0

for i in s:
    if i.lower() in "aeiou":
        count += 1

print("Vowels =", count)

#Find factorial of a number.
n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

#Reverse a string using loop.
s = input("Enter string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reversed string =", rev)

#Find sum of digits of a number.
n = int(input("Enter number: "))

total = 0

for i in str(n):
    total += int(i)

print("Sum of digits =", total)

#Print pyramid pattern.
# rows = 5

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))

n = int(input("Enter limit: "))
for i in range(1,n+1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)