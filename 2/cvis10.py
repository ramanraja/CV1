# copy a sub rectangle on an image

import cv2

img = cv2.imread('bm.jpg')
print img.shape

img[0:50, 10:100] =  img[100:150, 10:100]
cv2.imshow("My Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()