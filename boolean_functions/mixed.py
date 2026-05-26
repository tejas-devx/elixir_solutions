#Create a dictionary and check its length
d = {1:'Adhil',2:'Jyothish',3:'Tejas'}
print(len(d))

#Create two sets and perform union
s1={1,2,3,4}
s2={5,6,7,8}
print(s1.union(s2))

#Store boolean values inside a dictionary
d={0:'False',1:'True'}
print(d.values())

#Create a set and print it
s={1,2,3,4}
print(s)

#Compare two dictionary values
d1 = {'a': 10, 'b': 20, 'c': 30,'e':50}
d2 = {'a': 15, 'd': 25, 'c': 30}

if set(d1.values()) == set(d2.values()):
    print("values same")
else:
    print("values are different")