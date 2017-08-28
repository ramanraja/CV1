# Sobel edge detection for RGB channels

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

file_name = 'bluecar.png'
file_name = 'gradient8.png'
file_name = 'gradient9.png'
file_name = 'graycar.png'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
args = vars(ap.parse_args())
if not args['image']==None: file_name = args['image']
print file_name

img = cv2.imread(file_name)
#cv2.imshow('Original',img)

b,g,r = cv2.split(img)  
# 64 bit float to handle negative gradients    
sobelXr = cv2.Sobel(r, cv2.CV_64F, 1, 0)
sobelYr = cv2.Sobel(r, cv2.CV_64F, 0, 1)
sobelXr = np.uint8(np.absolute(sobelXr))
sobelYr = np.uint8(np.absolute(sobelYr))

sobelXg = cv2.Sobel(g, cv2.CV_64F, 1, 0)
sobelYg = cv2.Sobel(g, cv2.CV_64F, 0, 1)
sobelXg = np.uint8(np.absolute(sobelXg))
sobelYg = np.uint8(np.absolute(sobelYg))

sobelXb = cv2.Sobel(b, cv2.CV_64F, 1, 0)
sobelYb = cv2.Sobel(b, cv2.CV_64F, 0, 1)
sobelXb = np.uint8(np.absolute(sobelXb))
sobelYb = np.uint8(np.absolute(sobelYb))

sobelCombinedr = cv2.bitwise_or(sobelXr, sobelYr)
cv2.imshow("Sobel Red", np.hstack([sobelXr,sobelYr,sobelCombinedr]))

sobelCombinedg = cv2.bitwise_or(sobelXg, sobelYg)
cv2.imshow("Sobel Green", np.hstack([sobelXg,sobelYg,sobelCombinedg]))

sobelCombinedb = cv2.bitwise_or(sobelXb, sobelYb)
cv2.imshow("Sobel Blue", np.hstack([sobelXb,sobelYb,sobelCombinedb]))


cv2.waitKey(0)  
cv2.destroyAllWindows()