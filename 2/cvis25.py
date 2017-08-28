# Brighten/darken an image 

import cv2
import numpy as np
     
img = cv2.imread('photo.png')
cv2.imshow("Original", img)

mat = np.ones(img.shape, np.uint8)*100
img2 = cv2.add(img, mat) 
cv2.imshow("Brighter", img2)

mat = np.ones(img.shape, np.uint8)*50
img2 = cv2.subtract(img, mat)
cv2.imshow("Darker", img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



