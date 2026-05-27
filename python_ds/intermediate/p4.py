#Remove all even numbers from a list.
l = list(map(int,(input("Enter numbers: ").split())))

for i in l[:]:
    if i%2==0:
        print(i)
        l.remove(i)
print(l)

# l = list(map(int, input("Enter numbers: ").split()))

# l = [i for i in l if i % 2 != 0]

# print(l)