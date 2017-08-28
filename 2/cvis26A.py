# Blak & white images in cv2

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

#combined_canvas = cv2.hconcat(canvas2, canvas1)
#cv2.imshow("Both", combined_canvas)
 
cv2.waitKey(0)
cv2.destroyAllWindows()




