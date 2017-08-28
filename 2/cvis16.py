# draw random circles on a canvas

import numpy as np
from numpy import random as rand
import cv2

canvas = np.zeros((500, 500, 3), dtype = "uint8") # (y,x,3)

for i in range(25):
    (cx,cy) = rand.randint(0,500, size=(2,))
    (b,g,r) = rand.randint(0,255, size=(3,))
    rad = rand.randint(2,100)
    thickness = rand.randint(-1,4)
    cv2.circle(canvas, (cx,cy), rad, (b,g,r), thickness)

cv2.imshow("My Art", canvas)  # reuse the same window
cv2.waitKey(0)
cv2.destroyAllWindows()    