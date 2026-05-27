#Count frequency of each element in a list (use dictionary).

d ={

}

lst = input("Enter list: ").split()
for item in lst:
    if item in d:
      d[item] += 1  
    else:
       d[item] = 1
print(d)