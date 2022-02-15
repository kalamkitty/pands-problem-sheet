# program that reads a students % and prints our corresponding grade

from numpy import percentile


percentage = float(input("Enter the percentage:"))


# to print
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 to 100")
elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit 2")
elif percentage < 70:
    print ("Merit 1")
else:
    print ("Disinction")