#Find the first non-repeating element in a list.
l = list(map(int, input("Enter elements: ").split()))

for i in l:
    if l.count(i) == 1:
        print("First non-repeating element:", i)
        break