# Bilateral blur 
# preserves edges, while still reducing noise
# only pixels with similar intensity are included in the computation of blur

import cv2
import numpy as np
import argparse

file_name = "photo.png"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the image")
args = vars(ap.parse_args())
print args
if args['image']==None:
    args['image'] = file_name
    
img = cv2.imread(args['image'])

# parameters: image, neighbourhood diameter, color sigma, space sigma-subject to similarity of color
bilat1 = np.hstack([img, cv2.bilateralFilter(img, 7,21,21)])
bilat2 = np.hstack([cv2.bilateralFilter(img, 9, 31,31), cv2.bilateralFilter(img, 11,41,41)]) 
cv2.imshow("Bilateral Blur", np.vstack([bilat1, bilat2]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




