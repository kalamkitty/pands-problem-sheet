# Calculate somebody's Body Mass Index (BMI)
# Author: Ka Lam (Kitty) Kwan

# REF 1: Rounding with python
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

# REF 2: BMI calculator in Python
# https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g

weight = int(input('Enter your weight (kg):'))             # user to input weight and height
height = int(input('Enter your height (cm):'))

BMI = weight / (height/100)**2                             # calculates user's BMI

print ('The BMI is (kg/m**2) {:.2f}.'.format(BMI))         # returns BMI in 2 decimal places