# program prints out random fruit

import random
fruit = ['Apple', 'Banana', 'Orange', 'Pear']   #[] list

# random number between 0 and lenght-1
index = random.randint (0,len(fruit)-1)
fruit = fruit[index]
print("A random fruit: {}" .format (fruit))