# Split the channels and merge
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

import cv2
import numpy as np

img = cv2.imread("cars.jpg")
cv2.imshow("Original", img)
 
b,g,r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

comb = cv2.merge((b,g,r))   # takes a single tuple
cv2.imshow("Combined", comb)

comb2 = cv2.merge((g,r,b))  # shuffle the order
cv2.imshow("Shuffled", comb2)

cv2.waitKey(0)
cv2.destroyAllWindows()




