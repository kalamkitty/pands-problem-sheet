# Program that reads in a text file and outputs the number of e's it contains. Program should take the filename from an argument on the command line 
# Author: Kitty Kwan

# REF 1: Get file name from argument on command line
# https://stackoverflow.com/questions/16869467/command-line-arguments-reading-a-file
# https://stackoverflow.com/questions/33766029/python-command-line-arguments-file-name

# REF 2: Python file write
# https://www.w3schools.com/python/python_file_write.asp

# REF3: Letter frequancy in text file
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

#f = open("moby-dick.txt", "x")      # creates file
#f.write("116960")

import sys                          # import function
filename = sys.argv[-1]             # first command line argument passed to the script

def letterFrequency(fileName, letter):    # define function to return letter count        
    file = open(fileName, 'r')            # open file in read mode
    text = file.read()                    # store contents of file in variable
    return text.count(letter)             # using count function

print(letterFrequency(filename, 'e'))     # calling function and display the letter count









