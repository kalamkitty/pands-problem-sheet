# Program generates 10 random numbers, prints them out
# then prints out the top 3

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []
for i in range (0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}".format(howMany,numbers))

topOnes = numbers.copy()
topOnes.sort (reverse= True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))
