# Pands-Problem-Sheet: Weekly Tasks
## This repository is for weekly problem sheets for the Programming and Scripting Module


# Week 01 - Hello World

In the first task I wrote a simple program that prints out Hello World. Using the week's lecture as a guide.

References:

Weekly lecture and labs



# Week 02 - BMI calculator

In this task I wrote a program which asks the user to input their height and weight, converted the input to a float and output the user's BMI in 2 decimal places. I used the weekly lecture as reference and researched the BMI calculation. After the review, I added {:.2f} to round the output to two decimal places.

References:

Stack Overflow. 2013. How to round to 2 decimals with Python?. [online] Available at: <https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python> [Accessed 22 March 2022].

Singh, R., 2021. How to build a BMI Calculator in Python. [online] DEV Community. Available at: <https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g> [Accessed 2 February 2022].

# Week 03 - Second string

This program takes an input string from the user and outputs every second letter in reverse. I updated my code to slice the string once rather than twice after the interm feedback, using [::-2]. Which will count by every second letter in reverse.

References:

Stack Overflow. 2018. Python printing ever other letter of a word. [online] Available at: <https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word> [Accessed 10 February 2022].

Educative: Interactive Courses for Software Developers. n.d. How do you reverse a string in Python?. [online] Available at: <https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python> [Accessed 10 February 2022].

# Week 04 - Collatz

This program asks the user to input a positive integer and outputs the successive values of these calculations;

At each step, calculate the next value by taking the current value, if it's even, divide by 2, if it's odd, multiply by 3 and add 1. Using while loop, this program
runs until the number reaches 1. I added (end=' ') after the interim review to display output horizontally.

References:

Stack Overflow. 2016. Making a collatz program automate the boring stuff. [online] Available at: <https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff> [Accessed 15 February 2022].

Stack Overflow. 2015. Strings Iteration - Printing a String Horizontally. [online] Available at: <https://stackoverflow.com/questions/31900996/strings-iteration-printing-a-string-horizontally> [Accessed 22 March 2022].


# Week 05 - Weekday

This program uses the weekday function and return a message stating whether today is a weekday/weekend. Using date.weekday(), digits 0-6 represent consecutive days of the week, starting from monday.

References:

Python Programming. n.d. How to find current day is weekday or weekends in Python?. [online] Available at: <https://www.pythonprogramming.in/how-to-find-current-day-is-weekday-or-weekends-in-python.html> [Accessed 23 February 2022].


# Week 06 - Square root

This program gets the approximate square root of the users input, using Newton's method. I used this formula squareroot = 0.5 * (approx + (usersinput / x))  to get a broad estimate of the square root of the input number. Using a while loop to calculate a more accurate answer using the same formula, to only stop the process when the better estimate equals to the initial assumed estimate.

References:

Square Root of a Number using Newton's Method | Python | The Last Minute Professor. 2021. [video] Youtube.https://www.youtube.com/watch?v=xdlIFw5EM4w .

Stack Overflow. 2019. Newton's method for approximating square roots. [online] Available at: <https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots> [Accessed 21 March 2022].

# Week 07 - Count Es

This programs reads a text file and outputs the number of e's the file contains. I am assuming that only lower case e need to be counted, taking the sentence quite literally.
It took me a while to understand the task, but after looking through a few forums, I based the start of my code from the below stackoverflow answers. filename = sys.argv[-1]  takes the file name from an argument on the command line and used the lecture/lab/w3 notes to create a file moby-dick and open it in read mode. 

References:

Stack Overflow. 2013. Command line arguments, reading a file. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/16869467/command-line-arguments-reading-a-file> [Accessed 5 March 2022].

Stack Overflow. 2017. Python command line arguments file name. [online] Available at: <https://stackoverflow.com/questions/33766029/python-command-line-arguments-file-name> [Accessed 5 March 2022].

W3schools.com. n.d. Python File Write. [online] Available at: <https://www.w3schools.com/python/python_file_write.asp> [Accessed 5 March 2022].

GeeksforGeeks. 2021. Count the number of times a letter appears in a text file in Python - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/> [Accessed 5 March 2022].


# Week 08 - plotTask

This program plots 3 different mathematical functions in the range [0, 4] on the one set of axes. Using tutorialspoint.com's examples, I used the matplotlib.pyplot and numpy functions to plot the three given functions. I added labels to the axis and changed their colours using the color function.

References:
Stack Overflow. 2021. Adding a legend to PyPlot in Matplotlib in the simplest manner possible. [online] Available at: <https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible> [Accessed 28 March 2022].

Swcarpentry.github.io. n.d. Plotting – Plotting and Programming in Python. [online] Available at: <https://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html> [Accessed 28 March 2022].

Palomino, J. and Wasser, L., n.d. Customize Your Plots Using Matplotlib. [online] Earth Data Science - Earth Lab. Available at: <https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/> [Accessed 28 March 2022].

Tutorialspoint.com. n.d. NumPy - Matplotlib. [online] Available at: <https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm> [Accessed 28 March 2022].