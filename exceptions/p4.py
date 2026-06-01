#Write a program to take student marks and display grade while handling errors
try:
    mark = int(input("Enter mark: "))

    if mark < 0 or mark > 100:
        raise ValueError("Mark should be bw 0 and 100")
    
    if mark>=90:
        print("Grade A")

    elif mark>=75:
        print("Grade B")

    elif mark >=50:
        print("Grade C")

    else:
        print("Fail")

except ValueError as e:
    print(e)