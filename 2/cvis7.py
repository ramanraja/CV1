# change from BGR to RGB color space

import cv2
import numpy as np

img = cv2.imread('bm.jpg')
print img.size
print img.shape

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("My Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()