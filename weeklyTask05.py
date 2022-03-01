# program that outputs wheather or not today is a weekday

import datetime
 
weekno = datetime.datetime.today().weekday()
if weekno < 5:
    print("Yes, unfortuately today is a Weekday")
else:  # 5 Sat, 6 Sun
    print("It is the Weekend,yay!")