# Program that takes a float amount of $ and returns that absolute amount in cent
# Amount: -5.99, amount in cent: 599
# Author: Ka Lam(Kitty) Kwan


number = float(input('Enter an amount:'))
absoluteValue = abs (number*100)
print('The amount in cent is {}'.format (absoluteValue))