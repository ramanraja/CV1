# Bitwise operations

import cv2
import numpy as np

white = 255
black = 0
canvas1 = np.zeros((300,300), dtype='uint8')
cv2.rectangle (canvas1, (25,25),(275,275), white, -1)
cv2.imshow("Rectangle", canvas1)

canvas2 = np.zeros((300,300), dtype='uint8')
cv2.circle (canvas2, (150,150),148, white, -1)
cv2.imshow("Circle", canvas2)

and_canvas = cv2.bitwise_and(canvas1, canvas2)
cv2.imshow("AND", and_canvas)

or_canvas = cv2.bitwise_or(canvas1, canvas2)
cv2.imshow("OR", or_canvas)
 
xor_canvas = cv2.bitwise_xor(canvas1, canvas2)
cv2.imshow("XOR", xor_canvas)
 
not_canvas = cv2.bitwise_not(canvas2)
cv2.imshow("NOT", not_canvas)
 
cv2.waitKey(0)
cv2.destroyAllWindows()




