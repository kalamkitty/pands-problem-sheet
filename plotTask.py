# The program displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.
# Author: Kitty Kwan

# REF 1: Adding legends to plots 
# https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible

# REF 2: Plotting in python
# https://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html

# REF 3 : Customize plots in python
# https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/

 
import matplotlib.pyplot as plt 
import numpy as np                                                    # import libraries


x =np.array(range(0,5))                                               # array0, 1, 2, 3, 4, same for all three functions

y1 = x                                                                # f(x)=x
y2 = x**2                                                             # g(x)=x^2
y3 = x**3                                                             # h(x)=x^3                                     

plt.plot(x,y1, label="f(x)=x", color='green', linewidth = 3)          # plots f(x)=x , using color argument to set colour of plot
plt.plot(x,y2, label="g(x)=x^2", color='red', linewidth = 3)          # plots g(x)=x^2
plt.plot(x,y3, label="h(x)=x^3", color='blue', linewidth = 3)         # plots h(x)=x^3  

plt.legend(loc= "upper left")                                         # adding legend to plot
plt.title("Plot Task", color = 'black')                               # adding title to plot        
plt.xlabel("x", color ='black')                                       # labeling x axis                        
plt.ylabel("y (Functions of x) ", color = 'black')                    # labeling y axis     

plt.plot(range(5))
plt.xlim(0, 4)                                                        # x axis limit up to 4
plt.ylim(0, 64)                                                       # y axis limit up to 64 (4^3)

plt.show()                                                            # instruct matplotlib to show a figure
plt.savefig('plotTask.png')                                           # saving plot                        