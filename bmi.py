# Calculate somebody's Body Mass Index (BMI)
# Author: Ka Lam (Kitty) Kwan


weight = int(input('Enter your weight in kg:'))
height = int(input('Enter your height in cm:'))

x = (weight)
y = (height/100)*(height/100)
Z = x/y

print ('Hello \t Your BMI is {}'.format(Z))