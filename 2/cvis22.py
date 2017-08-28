# Resize an image

import cv2
     
img = cv2.imread('bm.jpg')
img2 = cv2.resize(img, (300,500), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", img2)
cv2.waitKey(4000)
cv2.destroyAllWindows()



