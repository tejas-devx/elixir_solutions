#Implement a simple hashmap using dictionary.
d = {}

n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    d[key] = value

print(d)