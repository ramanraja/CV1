# Read and disply using Open CV

import cv2

img = cv2.imread('bm.jpg')
print img.shape
cv2.imshow("Picture", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


