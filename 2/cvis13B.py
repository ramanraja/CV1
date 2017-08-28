# draw lines on a canvas

import numpy as np
import cv2
canvas = np.zeros((300, 400, 3), dtype = "uint8")

green = (0, 255, 0)
red = (0, 0, 255)

cv2.line(canvas, (0, 10), (200, 290), green)    # (x1,y1), (x2,y2)
cv2.line(canvas, (190, 290), (390, 10), red, 3)
cv2.imshow("My Art", canvas)  # create a single window
cv2.waitKey(0)
cv2.destroyAllWindows()