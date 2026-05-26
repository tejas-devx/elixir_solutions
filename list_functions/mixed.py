#Convert string → list using split() Then count words

l1 = input("Enter the list: ").split()
print(len(l1))

#Convert list → string using join()👉["I","love","python"]→"I love python"

l2 = ["I","love","python"]
print(' '.join(l2))

#Count vowels in list of strings 👉["apple","banana"]
l3 = input("Enter a list: ").lower().split()
count = 0
for v in l3:
    count += v.count('a')+v.count('e')+v.count('i')+v.count('o')+v.count('u')

print(count)

#Find common elements in two lists1
l4 = input("Enter a list: ").split()
l5 = input("Enter the second list: ").split()
for i in l4:
    if i in l5:
        print(i)

#Remove empty strings from list👉["a","","b","","c"]
l6 = ["a","","b","","c"]
for i in l6:
    if i =="":
        l6.remove(i)
print(l6)