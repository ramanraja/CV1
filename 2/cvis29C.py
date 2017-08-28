# Convert to HSV, split the channels and merge
# Example given in book 'Learning image processing with open cv'

import cv2
import numpy as np

img = cv2.imread("cars.jpg")
cv2.imshow("Original", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# split into HSV ? or still thinking it ai B,G,R ? 
h,s,v = cv2.split(img) 

cv2.imshow("Hue", h)  
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)

comb = cv2.merge((h,s,v))   # takes a single tuple as argument
cv2.imshow("Combined", comb)  # NOTE: original is not restored !

cv2.waitKey(0)
cv2.destroyAllWindows()




