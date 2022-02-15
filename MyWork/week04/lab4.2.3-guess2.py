# User to guess, program to tell user guess is too high/low (while loop)


numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")

    else:
        print("too high")

    guess = int(input("Please guess again:"))
print ("well done! Yes the number was", numberToGuess)