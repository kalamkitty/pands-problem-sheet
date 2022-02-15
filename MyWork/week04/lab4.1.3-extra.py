# percentages are rounded i.e.69.5 to 70 to a distinction, how to modify to deal with this?

percentage = float(input("Enter an percentage:"))   #float instead of int


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