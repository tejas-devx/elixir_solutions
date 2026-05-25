#Remove duplicate characters using functions
str = input("Enter a string ")
result = []
for i in str:
    if i not in result:
        result.append(i)

print(''.join(result))

#Reverse string using slicing
str1 = input("Enter a string ")
rev = str1[-1::-1]
print(rev)

#Check palindrome using functions

str2 = input("Enter a string ")
if str2 == str2[::-1]:
    print(str," is a pallindrome")
else:
    print(str2," not a pall indrome")

#Convert "hello world"→"hElLo WoRlD"(alternate case)
str3="hello world"
s=str3.lower()
d=list(s)
for i in range(1,len(s),2):
    d[i]=s[i].upper()
print("".join(d))

#Extract only alphabets from "abc123@#"
str4 = "abc123@#"
for i in str4:
    if i.isalpha():
        print(i)