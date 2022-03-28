# program that asks user to input +ive integer and outputs
# successive values of the following calculation;

# At each step, calculate next value by taking current value and if its even,
# divide by 2, but if its odd, multiply by 3 and add 1.
# Author : Ka Lam (Kitty) Kwan

# REF 1: Using the collatz function that allows user to enter integer, then create loop on the integer until the function returns the value 1
# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

# REF 2: Printing strings horizontally
# https://stackoverflow.com/questions/31900996/strings-iteration-printing-a-string-horizontally

def collatz(number):                 # creating function

    if number % 2 == 0:              # if number is an even number
        print(number //2,end=' ')    # divide by 2
        return  number / 2

    elif number % 2 == 1:            # if number is an add 
        result = number * 3 + 1      # multiple by 3 and add 1 
        print(result,end=' ')
        return result

n = input("Please enter a positive integer: ")    
while n != 1:                                      # loop will execute when the number becomes 1
    n = collatz(int(n))
