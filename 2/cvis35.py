# Otsu thresholding using cv2 (minimal code)

import cv2
img = cv2.imread('parking4.jpg',0)  # parameter 0 to convert into gray level 
ret,threshed =cv2.threshold(img,0,255,cv2.THRESH_OTSU)
print ret
cv2.imshow('Otsu',threshed)
cv2.waitKey(0)  
cv2.destroyAllWindows()