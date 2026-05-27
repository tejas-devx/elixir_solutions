#Find all pairs in a list whose sum is equal to a target.
l = list(map(int,input("Enter elements: ").split()))
target = int(input("Enter target: "))

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == target:
            print(l[i],l[j])