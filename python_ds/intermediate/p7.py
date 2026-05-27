#Find missing numbers in a sequence.
l = [1,2,3,4,5,6,7]
l1 = [1,2,4,5]

for i in l :
    if i not in l1:
        print(i)