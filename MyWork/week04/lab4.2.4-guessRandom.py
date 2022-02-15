# program to guess random number b/t 0-100 
# author: Ka Lam (Kitty) Kwan
numberToGuess = 30

import random              # generate number
numberA = random. randint(1,100)
print ("number guessed: {}". format (numberA))

if numberA == numberToGuess:
    print ("That's the right number!")
elif numberA > numberToGuess:
    print("Guessed too small")
elif numberA < numberToGuess:
    print("guessed too high")