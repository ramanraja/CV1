# convert from BGR to HSV using cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

img = cv2.imread('bm.jpg')
print img.size
print img.shape

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.show()