# Color histograms of a HSV image; takes input file from command line
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

file_name = "redcar.png"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])
print img.shape
cv2.imshow("Original", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# split into HSV ? or still thinking it ai B,G,R ? 
hsv = cv2.split(img) 
colours = ["B", "G", "R"]
zipped = zip(hsv, colours)

plt.figure()
plt.title('Histograms')

for (chl, col) in zipped:
    hist = cv2.calcHist([chl], [0], None, [256], [0,256])
    plt.xlim([-5, 260])
    #plt.ylim([0, 10000])  # adjust empirically for each picture
    plt.plot(hist, color=col)

plt.show()
 




