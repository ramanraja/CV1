# 2-D mask: ellipse shaped

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("photo.png")
print img.shape

h,w = img.shape[0],img.shape[1]
center = (w/2,h/2)
radii = (w/2-10, w/2-60)
mask_canvas = np.zeros((h,w), dtype='uint8')  

cv2.ellipse (img=mask_canvas, center=center, axes=radii , angle=45, startAngle=0, endAngle=320, color=150, thickness=-1)  
cv2.imshow("The Mask", mask_canvas)

img2 = cv2.bitwise_and(img, img, mask=mask_canvas)
cv2.imshow("Original", img) 
cv2.imshow("Masked", img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()




