# Color & grayscale histograms of a whole image
# (Not split into channels)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "graycar.png"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])
print img.shape

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.figure()
plt.title('Histograms')
plt.subplot(1,2,1)
plt.xlim([0, 260])
plt.plot(hist)
 
img = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE)
print img.shape

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.subplot(1,2,2)
plt.xlim([0, 260])
plt.plot(hist)
plt.show()
 
 




