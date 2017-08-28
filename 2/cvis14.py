# draw rectangles on a canvas

import numpy as np
import cv2
canvas = np.zeros((300, 400, 3), dtype = "uint8") # (y,x,3)

purple = (190,0,190)
green = (0, 255, 0)
red = (0, 0, 255)

cv2.rectangle(canvas, (10, 30), (100, 200), green, 3) # (x1,y1), (x2,y2)
cv2.rectangle(canvas, (390, 20), (50, 210), red)
cv2.rectangle(canvas, (250, 40), (380,100), purple, -5)

cv2.imshow("My Art", canvas)  
cv2.waitKey(0)
cv2.destroyAllWindows()