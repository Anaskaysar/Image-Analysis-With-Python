"""
sykit image
opencv

pillow //stay away
"""

from skimage import io,img_as_float,img_as_ubyte
img = io.imread('images/Osteosarcoma_01.tif')

print(img.shape) #y, x, c-rgb

img2= img_as_float(img)

img3=img_as_ubyte(img2)


#open cv
#OPEN CV READ THE IMAGES AS BGR AND SAVES AS BGR
import cv2

img_cv2=cv2.imread('images/Osteosarcoma_01.tif')
gray_img=cv2.imread('images/Osteosarcoma_01.tif',0)
color_img=cv2.imread('images/Osteosarcoma_01.tif',1)


img_opencv=cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB) #CONVERT AN BGR TO RGB USING OPEN CV



