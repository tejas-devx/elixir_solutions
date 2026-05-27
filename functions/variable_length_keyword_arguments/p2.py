#Create a function to print employee information

def employee(**kwargs):

    for k, v in kwargs.items():
        print(k, ":", v)


employee(name="Rahul", salary=50000, department="HR")