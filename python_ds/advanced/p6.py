#Group elements by frequency.
l = list(map(int, input("Enter elements: ").split()))

d = {}

for i in l:
    d[i] = d.get(i, 0) + 1

print(d)