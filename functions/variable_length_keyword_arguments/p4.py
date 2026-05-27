#Create a function to store customer information dynamically

def customer(**kwargs):

    for k, v in kwargs.items():
        print(k, ":", v)


customer(name="Anu", city="Kochi", phone=9876543210)