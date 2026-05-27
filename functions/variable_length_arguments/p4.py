#Create a function to calculate average of numbers.
def average(*args):

    avg = sum(args) / len(args)

    print("Average =", avg)


average(10, 20, 30, 40)