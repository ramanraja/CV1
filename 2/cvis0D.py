# Splice two images side by side  or up /down

import cv2
import numpy as np

img = cv2.imread('bm.jpg')
print img.shape

img2 = np.hstack([img, img])
cv2.imshow("np.hstack", img2)

img3 = np.vstack([img, img])
cv2.imshow("np.vstack", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


