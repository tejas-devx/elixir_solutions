#Check palindrome (number/string)
s =input("Enter value: ")

if s == s[::-1]:
    print("pallindrome")
else:
    print("Not pallindrome")