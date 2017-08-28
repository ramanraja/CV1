# Translation, left and up

import cv2
import numpy as np

img = cv2.imread('bm.jpg')
s = img.shape
print s

mat = np.float32 ([[1,0,-20], [0,1,-60]])
img =  cv2.warpAffine(img, mat, (s[1],s[0]))

cv2.imshow("Shifted",img)
cv2.waitKey(0)
cv2.destroyAllWindows()   