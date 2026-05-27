#Flatten a nested list.
nested =[[1,2,3],[4,5,6],[7,8,9]]
lst =[]
for i in nested:
    for j in i:
        lst.append(j)
print(lst)