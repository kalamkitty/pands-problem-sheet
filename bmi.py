# Calculate somebody's Body Mass Index (BMI)
# Author: Ka Lam (Kitty) Kwan

# REF 1: Rounding with python
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

# REF 2: BMI calculator in Python
# https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g

weight = int(input('Enter your weight (kg):'))             
height = int(input('Enter your height (cm):'))

BMI = weight / (height/100)**2                             # REF 2

print ('The BMI is (kg/m**2) {:.2f}.'.format(BMI))         # REF 1