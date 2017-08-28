# Laplacian grdients

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

file_name = 'photo.png'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required = False, help = "Path to the image")
args = vars(ap.parse_args())
if not args['image']==None: file_name = args['image']
print file_name
print cv2.IMREAD_GRAYSCALE

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original',img)
    
lap = cv2.Laplacian(img, cv2.CV_64F) # 64 bit float for negative gradients
print type(lap)
print lap.dtype
print lap.shape

cv2.imshow('Laplacian-float',lap)

lap2 = np.uint8(lap)
cv2.imshow('Laplacian-uint8',lap2)

lap3 = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian-uint8-Absolute',lap3)

cv2.waitKey(0)  
cv2.destroyAllWindows()