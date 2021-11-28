
"""
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("images/RGBY.jpg", 1)   #Color is BGR not RGB

plt.imshow(img)


#use cv2.resize. Can specify size or scaling factor.
#Resize images

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("original pic", img)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

"""
###################################
#Pixel values, split and merge channels, 
"""
import cv2

grey_img = cv2.imread("images/RGBY.jpg", 0) 
img = cv2.imread("images/RGBY.jpg", 1)   #Color is BGR not RGB

print(img.shape)     #(586, 415, 3)
print("Top left", img[0,0])    #Top left pixel
print("Top right", img[0, 400])  # Top right
print("Bottom Left", img[580, 0]) # Bottom left
print("Bottom right", img[580, 400])  # Bottom right

cv2.imshow("color pic", img)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

#Split and merging channels
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only


cv2.imshow("red pic", red)
cv2.waitKey(0)          
cv2.destroyAllWindows() 


#Or split all channels at once

b,g,r = cv2.split(img)

cv2.imshow("green pic", g)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

#to merge each image into bgr

img_merged = cv2.merge((b,g,r))

cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)          
cv2.destroyAllWindows() 
"""

######################
# Opencv offers Many libraries for image processing tasks
#Edge detection:
import cv2

img = cv2.imread("images/Osteosarcoma_01.tif", 0)
edges = cv2.Canny(img,100,200)   #Image, min and max values

cv2.imshow("Original Image", img)
cv2.imshow("Canny", edges)

cv2.waitKey(0)          
cv2.destroyAllWindows() 
