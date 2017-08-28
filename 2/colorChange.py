# change colors of cars and save in files

import cv2
import numpy as np

#img = cv2.imread("purplecar.png")
img = cv2.imread("redcar.png")
cv2.imshow("Original", img)     # red was the dominant color 
 
black = np.zeros(img.shape[0:2], dtype='uint8')
b,g,r = cv2.split(img)          # r has the largest data values

# give the dominant R-data to green (center place)
comb = cv2.merge((b,r,g))   
cv2.imshow("BRG", comb)
cv2.imwrite("greencar.png", comb)

comb = cv2.merge((r,g,b))   
cv2.imshow("RGB-Blue", comb)    # dominant: blue
cv2.imwrite("bluecar.png", comb)

comb = cv2.merge((r,g,r))       # dominant: blue,red 
cv2.imshow("RGR-Magenta", comb)  
cv2.imwrite("magentacar.png", comb)

comb = cv2.merge((r,r,b))       # dominant: blue,green 
cv2.imshow("RRB-Cyan", comb)  
cv2.imwrite("cyancar.png", comb)

comb = cv2.merge((b,r,r))       # dominant: green,red
cv2.imshow("BRR-Yellow", comb)  
cv2.imwrite("yellowcar.png", comb)

comb = cv2.merge((r,r,r))       # dominant: all
cv2.imshow("RRR-Gray", comb)  
cv2.imwrite("graycar.png", comb)

cv2.waitKey(0)
cv2.destroyAllWindows()




