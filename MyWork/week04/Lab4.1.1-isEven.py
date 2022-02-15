# program that asks user to enter a number and program will tell the user if it's even/odd

number = int(input("Enter an integer:"))

if (number % 2) == 0 :
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))