#Guess the number game.
secret = 7

while True:

    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct Guess")
        break

    else:
        print("Try Again")