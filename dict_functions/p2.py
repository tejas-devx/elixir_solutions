#Access a value using a key
dict1 ={}
n = int(input("Enter number of items: "))
for i in range(n):
    k,v = input("Enter key and value: ").split()
    dict1[k] = v
print(dict1)
value = input("Enter key to access: ")
print(dict1.get(value))