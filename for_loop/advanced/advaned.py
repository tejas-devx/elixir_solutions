#Find prime numbers in a range.
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):

    if num > 1:

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#Generate Fibonacci series.
n = int(input("Enter limit: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

#Find common elements in two lists using loop.
l1 = input("Enter list1 elements: ").split()
l2 = input("Enter list2 elements: ").split()

for i in l1:
    if i in l2:
        print(i)

#Count frequency of elements using loop.
l = input("Enter elements: ").split()

d = {}

for i in l:
    d[i] = d.get(i, 0) + 1

print(d)