#Append multiple elements using loop

# l1 = input("Enter elements in list: ").split()
# l2 = input("Enter element to append: ").split()

# for item in l2:
#     l1.append(item)

# print(l1)

#Sort list in descending order
# l3 = list(map(int,input("Enter list of numbers: ").split()))
# l3.sort(reverse = True)
# print(l3)

#Remove duplicates from list
# l4 = input("Enter elements to list: ").split()

# dup = []

# for item in l4:
#     if item not in dup:
#         dup.append(item)
# print(dup)

#Find second largest number
# l5 = list(map(int,input("Enter elements to the list: ").split()))
# l5.sort(reverse=True)
# print(l5[1])

#Copy a list using copy()
# l6 = input("Enter what is to be copied to list: ").split()
# l7 = l6.copy()
# print(l7)

#Merge two lists using +
# l8 = input("Enter the first list: ").split()
# l9 = input("Enter the second list: ").split()
# merged_list = l8 + l9
# print(merged_list)

#Check if element exists in list
l10 = input("Enter the elements: ").split()
l11 = input("Enter element to be checked: ")
if l11 in l10:
    print("Element exists")
else:
    print("Element not found")