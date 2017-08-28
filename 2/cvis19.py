# Translation, as a function

import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate(image, x,y):
    s = img.shape
    mat = np.float32 ([[1,0,x], [0,1,y]])
    img2 =  cv2.warpAffine(img, mat, (s[1],s[0]))
    return img2
    
img = cv2.imread('bm.jpg')

plt.subplot(2,2,1) # indexing is 1-based
plt.imshow(img)

plt.subplot(2,2,2)
img2 = translate(img, 10,50)
plt.imshow(img2)

plt.subplot(2,2,3)
img2 = translate(img, -10,-50)
plt.imshow(img2)

plt.subplot(2,2,4)
img2 = translate(img, 10,-50)
plt.imshow(img2)

plt.show()
