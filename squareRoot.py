# Square root using newton method
# Author: Kitty Kwan


# REF 1: Square root using Newton's Method
# https://www.youtube.com/watch?v=xdlIFw5EM4w

# REF 2: Newtons method for approximating square roots
# https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots

# Newtons method: Assuming an approximate value as a square root, should try to find a better value until the better value found is not the assumed approximate value

num = float(input("Please enter a positive number: "))                 # convert the user's input (integer) to a floating-point value
approx = 0.5 * num                                                     # Calculate an estimate/approximate of square root of the input 
better = 0.5* (approx + num / approx)                                 # Calculate a better estimation of the initial estimate      

while (better != approx):                                              # while the better estimate is not equal to the inital estimate value,
    approx = better                                                    # using loop to calculate even a better answer,
    better = 0.5 * (approx + num / approx)                             # stop the process when the value of better becomes equal to the assumed estimate value

print ("The square root of 14.5 is approx.{:.1f}.".format(better))     # Outputs the result/ square root, to one decimal place