
from matplotlib import image
from matplotlib import pyplot
import os

path = "/Users/jadencheung/Documents/GitHub/ROAR-Academy/Week Two Exercises/flag-square-500.png"
data = image.imread(path)

# Read an image file
lennapath = os.path.dirname(os.path.abspath(__file__))
print(lennapath)
filename = lennapath + '/' + 'lenna.bmp'
lennadata = image.imread(filename)

flag_plot_data = data.copy()
plot_data = lennadata.copy()
for height in range(len()):
    for width in range(len(plot_data)-1-len(data)):
        plot_data[height][width] = flag_plot_data[height][width]
        

# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)


# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()



# use pyplot to plot the image
# pyplot.imshow(data)
# pyplot.show()

