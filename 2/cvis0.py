# load an image with cv2, but display with pyplot: R and B are interchanged
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bm.jpg')
print img.shape
plt.imshow(img) # note that it is all blue !
plt.show()


