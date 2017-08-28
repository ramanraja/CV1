# Apply a 2-D mask to an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("photo.png")
plt.imshow(img[:, :, (2,1,0)])
plt.show()

TL, BR = (112,176), (178,207) # empirically found from the above display

h,w = img.shape[0],img.shape[1]
mask_canvas = np.zeros((h,w), dtype='uint8')
cv2.rectangle (mask_canvas, TL,BR, 255, -1)

img2 = cv2.bitwise_and(img, img, mask=mask_canvas)
cv2.imshow("Masked", img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()




