# Gaussian Blur 

import cv2
import numpy as np

img = cv2.imread ("bm.jpg")

blurred = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow("Gaussian", blurred)
 
cv2.waitKey(0)
cv2.destroyAllWindows()




