#Create a function evenodd(num) to check whether a number is even or odd.

def evenodd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num = int(input("Enter a number: "))
evenodd(num)