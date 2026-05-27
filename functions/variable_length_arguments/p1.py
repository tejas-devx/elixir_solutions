#Write a function to find sum of any number of values.

def sum(*args):
    total = 0
    for i in args:
        total+=i
    print("Sum =",total)
a = map(int,input("Enter numbers: ").split())
sum(*a)