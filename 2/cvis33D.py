# Comparing averaging with Gaussian blur 

import cv2
import numpy as np

img = cv2.imread ("peppersalt.jpg") #("bm.jpg")

ave = np.hstack([cv2.blur(img, (3,3)), cv2.blur(img, (5,5)), cv2.blur(img, (9,9))])
blurred = np.hstack([cv2.GaussianBlur(img, (3,3),0), cv2.GaussianBlur(img, (5,5),0), cv2.GaussianBlur(img, (9,9),0)])
cv2.imshow("Avg Vs Gaussian", np.vstack([ave, blurred]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




