# program that outputs wheather or not today is a weekday
# Author: Kitty Kwan

# REF 1 : Find current day is weekday/weekend
# https://www.pythonprogramming.in/how-to-find-current-day-is-weekday-or-weekends-in-python.html

import datetime                                            # import daytime module
 
weekno = datetime.datetime.today().weekday()               # import today as a variable
if weekno < 5:                                             # if day is less than 5 (weekday) , print
    print("Yes, unfortuately today is a weekday")
else:                                                      # 5 Sat, 6 Sun, or else, print
    print("It is the weekend,yay!")