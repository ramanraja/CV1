# show an image with pyplot. Note that red and blue are interchanged
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bm.jpg')
plt.imshow(img)
plt.show()

