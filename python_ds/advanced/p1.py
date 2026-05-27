#Rotate a list by k positions.
l = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

k = k % len(l)

rotated = l[-k:] + l[:-k]

print(rotated)