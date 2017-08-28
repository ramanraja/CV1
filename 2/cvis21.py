# Rotation as a function, with color space correction

import cv2
import numpy as np
import matplotlib.pyplot as plt

def rotate(image, center, angle, cscorrect=True):
    s = img.shape
    mat = cv2.getRotationMatrix2D(center, angle, 1.0) # 1.0 is the scaling factor
    img2 = cv2.warpAffine(img, mat, (s[1],s[0]))  # width, height
    if cscorrect:
        img2[:,:,] = img2[:,:,(2,1,0)]  
    return img2
    
img = cv2.imread('bm.jpg')

center = (img.shape[1]/2, img.shape[0]/2)
plt.subplot(2,2,1) # indexing is 1-based
plt.imshow(img)

plt.subplot(2,2,2)
img2 = rotate(img, center, 45)
plt.imshow(img2)

plt.subplot(2,2,3)
img2 = rotate(img, center, 90)
plt.imshow(img2)

plt.subplot(2,2,4)
img2 = rotate(img, center, -90)
plt.imshow(img2)

plt.show()
