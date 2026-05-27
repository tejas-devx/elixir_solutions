#Create a dictionary from two lists (keys + values).
keys = input("Enter keys list: ").split()
values = input("Enter value list: ").split()
d = {
    
}
for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)