# floors a number - takes in a float and outputs a rounded down int

import math
numberToFloor = float(input('Enter a float number:'))
flooredNumber = math.floor(numberToFloor)
print('{} floored is {}'.format(numberToFloor,flooredNumber))