# draw lines on a canvas

import numpy as np
import cv2
canvas = np.zeros((300, 400, 3), dtype = "uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("My Art", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("My Art", canvas)  # reuse the same window
cv2.waitKey(0)
cv2.destroyAllWindows()