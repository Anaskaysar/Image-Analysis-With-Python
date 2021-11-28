"""
#This code shows that unsharp is nothing but original + amount *(original-blurred)
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

img = img_as_float(io.imread("images/sandstone_blur_2sigma.tif", as_gray=True))

gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

img2 = (img - gaussian_img)*2.

img3 = img + img2

from matplotlib import pyplot as plt
plt.imshow(img, cmap="gray")
plt.imshow(img2, cmap="gray")
plt.imshow(img3, cmap="gray")


"""
from skimage import io
from skimage.filters import unsharp_mask

img = io.imread("images/sandstone_blur_2sigma.tif")

#Radius defines the degree of blurring
#Amount defines the multiplication factor for original - blurred image
unsharped_img = unsharp_mask(img, radius=3, amount=2)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(unsharped_img, cmap='gray')
ax2.title.set_text('Unsharped Image')

plt.show()
