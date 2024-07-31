
from matplotlib import image
from matplotlib import pyplot

path = "/Users/jadencheung/Documents/GitHub/ROAR-Academy/Week Two Exercises/flag-square-500.png"
data = image.imread(path)




# use pyplot to plot the image
pyplot.imshow(data)
pyplot.show()

