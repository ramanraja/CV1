# Histogram equalization
# It is done on gray scale images to improve contrast

import cv2
import numpy as np
import argparse

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
cv2.waitKey(0)
cv2.destroyAllWindows()


