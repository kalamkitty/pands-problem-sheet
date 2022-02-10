# program that prints out a random number between 1 and 10

import random
number = random.randint(1,10)
print("Here is a random number {}".format (number))

# program that prints out a random number between input range

import random
x = int(input (" Enter a number in the lower end of range: "))
y = int(input ("Enter a number in the top end of range: "))
number = random.randint(x,y)
print("Here is a random number {}".format (number))