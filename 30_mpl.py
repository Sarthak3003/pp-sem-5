
##BAR
import matplotlib.pyplot as plt

# x-coordinates of the bars
x = [1, 2, 3, 4, 5]

# heights of the bars
heights = [10, 20, 30, 40, 50]

# create the bar chart
plt.bar(x, heights)

# show the plot
plt.show()

##PIE
import matplotlib.pyplot as plt

# sizes of each slice of the pie
sizes = [10, 20, 30, 40, 50]

# labels for each slice of the pie
labels = ['A', 'B', 'C', 'D', 'E']

# create the pie chart
plt.pie(sizes, labels=labels)

# show the plot
plt.show()

##scatter
import matplotlib.pyplot as plt

# x-coordinates of the points
x = [1, 2, 3, 4, 5]

# y-coordinates of the points
y = [10, 20, 30, 40, 50]

# create the scatter plot
plt.scatter(x, y)

# show the plot
plt.show()

##HISTOGRAM
import matplotlib.pyplot as plt

# values to be plotted in the histogram
values = [10, 20, 30, 40, 50]

# create the histogram
plt.hist(values)

# show the plot
plt.show()

##