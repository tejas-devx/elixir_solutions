#Check if a number is positive, negative, or zero

n = int(input("Enter a number: "))

if n>0:
    print("Positive")
else:
    if n<0:
        print("Negative")
    else:
        print("Zero")