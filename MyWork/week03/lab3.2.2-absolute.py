# gives an absolute value of a number (i.e -4/4 would both output 4)

# ambiguous number but output implies that we are dealing with floats
# so we are casting the imput to a float


number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}:'.format(number,absoluteValue))
