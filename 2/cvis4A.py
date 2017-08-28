# show an image with pyplot.How to put red and blue in their correct positions

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bm.jpg')
print img.size
print img.shape
plt.imshow(img[:, :, (2,1,0)])  # make it R,G,B
plt.axis('off')
plt.show()

