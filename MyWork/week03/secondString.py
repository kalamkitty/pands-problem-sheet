# A program that asks a user to input a string and outputs every second letter in reverse order
# Author: Ka Lam (Kitty) Kwan

string = input ("Please enter a sentence:")[::-1]
secondString = string[::2]
print (secondString)