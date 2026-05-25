#Sort list without using sort()

#Find frequency of each element (use list + dictionary)
numbers = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for item in numbers:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)

#Remove all occurrences of a value
l3 = input("Enter the elements: ").split()
value = input("Enter the value")

while value in l3:
    l3.remove(value)
print(l3)

#Rotate list👉[1,2,3,4]→[2,3,4,1]
l4 = [1,2,3,4]
first = l4.pop(0)
l4.append(first)
print(l4)

#Split list into even and odd numbers
l5 = list(map(int,input("Enter the list: ").split()))
even = []
odd = []
for item in l5:
    if item % 2 ==0:
        even.append(item)
    else:
        odd.append(item)

print("Even numbers are: ",even)
print("Odd numbers are: ",odd)