
from matplotlib import image
from matplotlib import pyplot

path = "/Users/jadencheung/Documents/GitHub/ROAR-Academy/Week Two Exercises/flag-square-500.png"
data = image.imread(path)

plot_data = data.copy()
for width in range(512):
    for height in range(10):
        plot_data[height][width] = [255, 0, 0]   # Alternatively plot_data[height][width][:] = [255, 0, 0]
        plot_data[511-height][width] = [0,0,255]

# Write the modified images
image.imsave(path, plot_data)


# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()

