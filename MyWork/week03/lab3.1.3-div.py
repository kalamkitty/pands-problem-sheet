# program that reads in two numbers, divides first number by second number and
# outputs the integer result and remainder

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = int(x//y)   # // int division
remainder = x%y      # % remainder

print("{} divided by {} is {} with remainder {}".format (x, y, answer, remainder))
