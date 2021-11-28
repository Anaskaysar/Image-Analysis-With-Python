
"""
matplotlib.pyplot contains various functions for plotting, including images. 

Each pyplot function makes a change to the plot (e.g. add titles, labels, plots)
"""
#PLot using lists
from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y)  #plot takes any number of arguments


#Also understands numpy arrays
import numpy as np
a = np.array(x)
b = np.array(y)
plt.plot(a,b)


import cv2
gray_img = cv2.imread('images/sandstone.tif', 0)

plt.imshow(gray_img, cmap="gray")

plt.hist(gray_img.flat, bins=100, range=(0,150)) 
plt.bar(gray_img.flat, bins=100, range=(0,150)) 
#.flat is used for turning 2d array which is image a flat number for histogram


