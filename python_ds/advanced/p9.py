#Detect duplicates efficiently.
l = list(map(int, input("Enter elements: ").split()))

seen = set()
duplicates = set()

for i in l:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicates:", list(duplicates))