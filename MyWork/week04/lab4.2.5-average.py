# This program reads in numbers until the user enters 0
# it will them print numbers out and get their avg

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))
while number != 0:
 numbers.append(number)
 number = int(input("enter another (0 to quit): "))
for value in numbers:
 print (value)

average = float(sum(numbers)) / len(numbers)   # avg in a float
print ("The average is {}".format(average))