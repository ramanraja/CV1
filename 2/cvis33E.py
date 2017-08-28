# Median blur 
# useful to remove pepper salt noise

import cv2
import numpy as np
import argparse

file_name = "peppersalt.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])

med1 = np.hstack([img, cv2.medianBlur(img, 3)])
med2 = np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]) 
cv2.imshow("Median Blur", np.vstack([med1, med2]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




