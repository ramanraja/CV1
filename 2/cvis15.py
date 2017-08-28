# draw circles on a canvas

import numpy as np
import cv2
canvas = np.zeros((300, 300, 3), dtype = "uint8") # (y,x,3)

cx, cy = canvas.shape[1]/2, canvas.shape[0]/2

blue = [250,0,0]
for rad in range(0,150,20): 
    cv2.circle(canvas, (cx,cy), rad, blue)
    
cv2.imshow("My Art", canvas)  # reuse the same window
cv2.waitKey(0)
cv2.destroyAllWindows()