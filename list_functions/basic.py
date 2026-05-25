# append()
l1 = input("Enter a list: ").split()
l1.append("orange")
print(l1)

# insert()
l2 = input("Enter a list: ").split()
l2.insert(1,"grapes")
print(l2)

# remove
l3 = input("Enter a list: ").split()
l3.remove("banana")
print(l3)

# pop
l4 = input("Enter a list: ").split()
l4.pop()
print(l4)

# len()
l5 = len(input("Enter a list: ").split())
print(l5)

# count()
l6 = input("Enter a list: ").split()
print(l6.count("2"))

# sort()
l7 = list(map(int, input("Enter a list: ").split()))
l7.sort()
print(l7)

# reverse()
l8 = input("Enter a list: ").split()
l8.reverse()
print(l8)