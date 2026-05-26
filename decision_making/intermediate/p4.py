#Check if a number is divisible by both 3 and 5
n = int(input("Enter a number: "))

if n%3==0 and n%5==0:
    print("Divisible")
else:
    print("Not divisible")