# Split the channels, shuffle R,G,B and merge

import cv2
import numpy as np

img = cv2.imread("cars.jpg")
cv2.imshow("Original", img)
 
b,g,r = cv2.split(img)

comb1 = cv2.merge((b,r,g))  # shuffle the order
cv2.imshow("BRG", comb1)

comb2 = cv2.merge((r,g,b))   
cv2.imshow("RGB", comb2)

comb3 = cv2.merge((g,b,r))  
cv2.imshow("GBR", comb3)

cv2.waitKey(0)
cv2.destroyAllWindows()




