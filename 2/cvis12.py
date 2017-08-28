# change color of white areas to red 

import cv2
import numpy as np

img = cv2.imread('photo.png')
s = img.shape
print s

(b,g,r) = img[0,0,]
print b,g,r
print np.dtype(b)  # it can hold only 8 bits

for y in range(s[0]):
    for x in range(s[1]):
        (b,g,r) = img[y,x,]
        # if pixel is near-white, make it red
        if (int(r)+int(g)+int(b) > 3*250):     # note the upward casting from uint8
            img[y,x,] = (0,0,190)             # note it is stored column first in np array
 
cv2.imshow("My Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()