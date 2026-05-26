#Check Armstrong number

num = int(input("Enter number: "))
temp = num
sum = 0

while temp>0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if num == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")