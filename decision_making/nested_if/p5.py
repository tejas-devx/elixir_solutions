#Check discount eligibility based on amount

amount = int(input("Enter purchase amount: "))

if amount>=5000:
    if amount >= 10000:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")