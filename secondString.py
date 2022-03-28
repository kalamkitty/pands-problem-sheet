# A program that asks a user to input a string and outputs every second letter in reverse order
# Author: Ka Lam (Kitty) Kwan

# REF 1: Printing every other letter of a word
# https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word

# REF 2 : Reverse a string/ slicing
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python


string = input ("Please enter a sentence: ")[::-1]   # user's input as a string and reversing it
secondString = string[::2]                           # slicing the string and to print in reverse order
print (secondString)