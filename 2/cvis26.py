# Specifying colors in pyplot

import cv2
import numpy as np
import matplotlib.pyplot as plt

white = 255  # this will work only in cv2.imshow()
black = 0
canvas1 = np.zeros((300,300), dtype='uint8')
cv2.rectangle (canvas1, (25,25),(275,275), white, -1)
plt.subplot(2,2,1)
plt.imshow(canvas1)   # blue and red

canvas2 = np.zeros((300,300), dtype='uint8')
cv2.circle (canvas2, (150,150),148, white, -1)
plt.subplot(2,2,2)
plt.imshow(canvas2)

white = [255,255,255]
black = [0,0,0]

canvas3 = np.zeros((300,300,3), dtype='uint8')
cv2.rectangle (canvas3, (25,25),(275,275), white, -1)
plt.subplot(2,2,3)
plt.imshow(canvas3)

canvas4 = np.zeros((300,300,3), dtype='uint8')
cv2.circle (canvas4, (150,150),148, white, -1)
plt.subplot(2,2,4)
plt.imshow(canvas4)

plt.show() 
 



