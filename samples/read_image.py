## This is course material for Introduction to Python Scientific Programming
## Example code: read_image.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please do <pip3 install matplotlib> and <pip3 install pillow> first
from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

#read flag file
ipath = "/Users/jadencheung/Documents/GitHub/ROAR-Academy/samples/flag-square-500.png"
ifilename = ipath 
idata = image.imread(ifilename)

# Display image information
print('Image type is: ', type(idata))
print('Image shape is: ', idata.shape)

# Add some color boundaries to modify an image array
plot_data = idata.copy()
for width in range(512):
    for height in range(10):
        plot_data[height][width] = [255, 0, 0]   # Alternatively plot_data[height][width][:] = [255, 0, 0]
        plot_data[511-height][width] = [0,0,255]

# Write the modified images
#image.imsave(ipath+'/'+'lenna-mod.jpg', plot_data)
image.imsave(ipath)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()