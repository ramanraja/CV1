# Do histogram equalization & plot the histogram
# It is done on gray scale images to improve contrast

import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

file_name = "group.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])
print img.shape 

# convert to grayscale before equalizing
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print img.shape 

equalized = cv2.equalizeHist(img)
cv2.imshow("Histogram Equalization", np.hstack([img, equalized]))

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.subplot(1,2,1)
plt.xlim([-1, 256])
plt.plot(hist)

hist = cv2.calcHist([equalized], [0], None, [256], [0,256])
plt.subplot(1,2,2)
plt.xlim([-1, 256])
plt.plot(hist)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


