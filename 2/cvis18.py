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
img = translate(img, 10,50)
plt.imshow(img)
plt.show()
