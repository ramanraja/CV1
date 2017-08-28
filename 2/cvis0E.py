# Splice 4 images together

import cv2
import numpy as np

img = cv2.imread('bm.jpg')
print img.shape

img2 = np.hstack([img, img])
img3 = np.vstack([img2, img2])
cv2.imshow("np.vstack", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


