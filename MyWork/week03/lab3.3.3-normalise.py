# this program reads in a string and strips any leading/trailing spaces.
# converts all letters to lower case.
# outputs the length of original string and normalised one.

rawString = input('Please enter a string:')
normalisedString = rawString.strip ().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("The string normalised is: {}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(lengthOfRawString,lengthOfNormalised))