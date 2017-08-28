# Flip an image 

import cv2
     
img = cv2.imread('hadoop.png')
cv2.imshow("Original", img)

img2 = cv2.flip(img, 0) # horizontal
cv2.imshow("Flipped Horizontal", img2)

img2 = cv2.flip(img, 1) # vertical
cv2.imshow("Flipped Vertical", img2)

img2 = cv2.flip(img, -1) # both ways
cv2.imshow("Flipped both", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()



