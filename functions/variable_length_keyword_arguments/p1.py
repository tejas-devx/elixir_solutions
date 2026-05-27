#Write a function to display student details using *kwargs

def student(**kwargs):

    for k, v in kwargs.items():
        print(k, ":", v)


name = input("Enter name: ")
course = input("Enter course: ")
mark = int(input("Enter mark: "))

student(name=name, course=course, mark=mark)