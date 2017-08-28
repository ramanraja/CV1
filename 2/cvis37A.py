# Laplacian grdients for RGB channels

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
cv2.imshow('Original',img)
b,g,r = cv2.split(img)
    
# 64 bit float to handle negative gradients    
lapb = cv2.Laplacian(b, cv2.CV_64F) 
lapg = cv2.Laplacian(g, cv2.CV_64F) 
lapr = cv2.Laplacian(r, cv2.CV_64F)  

cv2.imshow('Laplacian-Red',np.uint8(np.absolute(lapr)))
cv2.imshow('Laplacian-Green',np.uint8(np.absolute(lapg)))
cv2.imshow('Laplacian-Blue',np.uint8(np.absolute(lapb))) 

cv2.waitKey(0)  
cv2.destroyAllWindows()