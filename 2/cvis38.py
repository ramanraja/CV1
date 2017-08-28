# Sobel edge detection for RGB channels: (keep colors !)

import cv2
import numpy as np
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
cv2.imshow('Original',img)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)  
cv2.destroyAllWindows()