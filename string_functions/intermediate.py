# Convert string to lowercase and count vowels
vowels = "a,e,i,o,u"
str = input("Enter a string").lower()
count = 0
for v in vowels:
    count += str.count(v)

print(str)
print(count)

str ="VOWELS"
lwr = str.lower()
print(lwr.count('a')+lwr.count('e')+lwr.count('i')+lwr.count('o')+lwr.count('u'))

#Remove spaces and find length
counts = len(input("Enter string").replace(" ",""))
print(counts)


#Replace spaces with _ and convert to uppercase
str ="Jy othi sh"
print(str.replace(" ","_").upper())


str =input("Enter a string").split()
for i in str:
    print(i)

#Find longest word using split()
str = input("Enter a string").split(" ")
larg = 0 
for i in str:
    if larg < len(i):
        larg = len(i)
        s = i
print(s)

#Check if substring exists using find()
s1 = input("Enter a string: ")
s3 = input("Enter substring to find: ")
if s1.find(s3) != -1:
    print("exist")
else:
    print("not exist")