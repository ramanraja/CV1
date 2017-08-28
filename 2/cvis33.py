# Blur an image: Averaging

import cv2
import numpy as np

img = cv2.imread ("bm.jpg")

ave = cv2.blur(img, (9,9))
cv2.imshow("Averaged", ave)
 
cv2.waitKey(0)
cv2.destroyAllWindows()




