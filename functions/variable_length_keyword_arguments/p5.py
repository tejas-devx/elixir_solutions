#Write a function that accepts any number of keyword arguments and prints them.

def details(**kwargs):

    for k, v in kwargs.items():
        print(k, ":", v)


details(a=10, b=20, c=30)