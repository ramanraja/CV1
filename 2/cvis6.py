# difference between size an shape of an image

import cv2

img = cv2.imread('police.jpg')
print img.size   # byte size; slightly larger than the file size
print img.shape  # y,x  or rows, cols

cv2.imshow("My Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()