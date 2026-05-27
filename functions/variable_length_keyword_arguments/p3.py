#Write a function to display product details

def product(**kwargs):

    for k, v in kwargs.items():
        print(k, ":", v)


product(name="Laptop", price=55000, brand="Dell")