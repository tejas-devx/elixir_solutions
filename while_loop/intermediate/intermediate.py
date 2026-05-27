#Check if a number is palindrome.
num = int(input("Enter number: "))

temp = num
rev = 0

while num > 0:
    digit = n % 10
    rev = rev * 10 + digit
    nnum = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")


#Count digits in a number.
n = int(input("Enter a number: "))
count = 0

while(n>0):
    r = n%10
    count +=1
    n=n//10
print(count)

#Find factorial using while loop.
factn = int(input("Enter the number")) #5
fact = 1 
i=1
while i<=factn: #1<=5 
    fact = fact*i #fact = 1*1
    i+=1 #2
print(fact)

#Sum of digits of a number.
n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits =", total)

#Generate Fibonacci series.
n = int(input("Enter limit: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    i += 1