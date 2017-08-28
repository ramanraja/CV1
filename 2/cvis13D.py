# draw text on a canvas

import numpy as np
import cv2
canvas = np.zeros((250, 400, 3), dtype = "uint8") # (y,x)

white = (255,255,255)
fon = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, "hello world", (10,150), fon, 2, white, 3, cv2.LINE_AA)    
cv2.imshow("Hello", canvas)   
cv2.waitKey(0)
cv2.destroyAllWindows()