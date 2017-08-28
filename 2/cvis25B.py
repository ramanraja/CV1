# Color filters using bitwise operations

import cv2
import numpy as np
     
img = cv2.imread('photo.png')
cv2.imshow("Original", img)
print img.shape

mat = np.ones(img.shape, np.uint8) 
mat[: ,:, 0] *= 0
img2 = cv2.bitwise_and(img, img, mask=mat) 
cv2.imshow("No blue", img2)

mat = np.ones(img.shape, np.uint8) 
mat[: ,:, 1] *= 0
img2 = cv2.add(img, mat) 
cv2.imshow("No Green", img2)
 
mat = np.ones(img.shape, np.uint8) 
mat[: ,:, 2] *= 0
img2 = cv2.add(img, mat) 
cv2.imshow("No Red", img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



