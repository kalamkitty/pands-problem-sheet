# Keeps promting user for a number until user enters -1
# Author: Ka Lam (Kitty) Kwan

number = int(input("Enter -1:"))

if (number % 2) == -1 :
    print("number is -1")
else:
    print("Thats incorrect")
    val = input ("please enter -1:")
    while val!= '-1':
        print ("you said:"+ val)
        val = input("please enter -1:")