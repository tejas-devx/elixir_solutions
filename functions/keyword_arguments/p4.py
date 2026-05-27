#Write a function person(name, city) and display details.
def person(name, city):
    print("Name:", name)
    print("City:", city)


name = input("Enter name: ")
city = input("Enter city: ")

person(city=city, name=name)