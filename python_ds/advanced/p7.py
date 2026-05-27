#Find intersection of multiple lists.
l1 = list(map(int, input("Enter list1: ").split()))
l2 = list(map(int, input("Enter list2: ").split()))
l3 = list(map(int, input("Enter list3: ").split()))

result = list(set(l1) & set(l2) & set(l3))

print(result)