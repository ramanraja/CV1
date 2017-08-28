# Color histogram of the 3 channels - needs debugging

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "jurassic.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image'] is not None:
    file_name = args['image']
print file_name
    
img = cv2.imread(file_name)
assert (img is not None), "File not found"
print img.shape
cv2.imshow("Imge", img)

# combine 3 histograms in one list (does not behave as expected) ***
hist = cv2.calcHist([img], [0,1,2], None, [32,32,32], [0,256, 0,256, 0,256])
print hist.shape    # something is wrong: it is a 32x32x32 array
print hist[0].shape

plt.figure()
plt.title('Histograms')
plt.xlim([-1, 33])
#plt.ylim([0, 10000])  # adjust empirically for each picture
plt.plot(hist[0], color='b')
plt.plot(hist[1], color='g')
plt.plot(hist[2], color='r')
plt.show()

 




