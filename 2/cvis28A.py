# 2-D mask: any non zero number will do

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("photo.png")
print img.shape
#plt.imshow(img[:, :, (2,1,0)])
#plt.show()

TL, BR = (50,130), (250,240) 

h,w = img.shape[0],img.shape[1]
mask_canvas = np.zeros((h,w), dtype='uint8')

cv2.rectangle (mask_canvas, TL,BR, 1, -1)

#cv2.rectangle (mask_canvas, TL,BR, 0,   -1)   # image is blacked out
#cv2.rectangle (mask_canvas, TL,BR, 256, -1)   # OK ! saturates to 255

img2 = cv2.bitwise_and(img, img, mask=mask_canvas)

cv2.imshow("Original", img) 
cv2.imshow("Masked", img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()




