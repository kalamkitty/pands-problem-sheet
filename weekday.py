# program that outputs wheather or not today is a weekday
# Author: Kitty Kwan

# REF 1 : Find current day is weekday/weekend
# https://www.pythonprogramming.in/how-to-find-current-day-is-weekday-or-weekends-in-python.html

import datetime
 
weekno = datetime.datetime.today().weekday()               # REF 1
if weekno < 5:
    print("Yes, unfortuately today is a weekday")
else:                                                      # 5 Sat, 6 Sun
    print("It is the weekend,yay!")