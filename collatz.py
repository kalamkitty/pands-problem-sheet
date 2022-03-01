# program that asks user to input +ive integer and outputs
# successive values of the following calculation;

# At each step, calculate next value by taking current value and if its even,
# divide by 2, but if its odd, multiply by 3 and add 1.

# Input 10, output should be: 10 5 16 8 2 1
# Author : Ka Lam (Kitty) Kwan

def collatz(number):

    if number % 2 == 0:        # Even number
        print(number // 2)
        return number // 2

    elif number % 2 == 1:      # Odd number
        result = number * 3 + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))