# Crop an image through numpy

import cv2
     
img = cv2.imread('bm.jpg')
cv2.imshow("Original", img)

img2 = img[5:120, 80:110]  #  [y1:y2, x1:x2] 
cv2.imshow("Crop !", img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



