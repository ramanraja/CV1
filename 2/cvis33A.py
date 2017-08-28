# Blur an image; stich the images side by side for display

import cv2
import numpy as np

img = cv2.imread ("bm.jpg")

ave1 = np.hstack([img, cv2.blur(img, (3,3))])
ave2 = np.hstack([cv2.blur(img, (7,7)), cv2.blur(img, (11,11))])
cv2.imshow("Averaged", np.vstack([ave1, ave2]))
 
cv2.waitKey(0)
cv2.destroyAllWindows()




