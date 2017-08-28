# draw Polygons on a canvas

import numpy as np
import cv2
canvas = np.zeros((250, 300, 3), dtype = "uint8") # (y,x)

red = (0, 0, 255)
green = (0,255,0)
# it is an array of arrays
points = np.array([[10,10], [20,100], [290,100], [290,200], [100,150]], np.int32)
cv2.polylines(canvas, [points], False, red, 5)    # note the squre bracket around points
cv2.polylines(canvas, [points], True, green, 1)    
cv2.imshow("Cubism", canvas)   
cv2.waitKey(0)
cv2.destroyAllWindows()