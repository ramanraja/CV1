# Take a picture, cut a circular piece and mask out the exterior  

import numpy as np
import cv2

def getFrame((cx,cy,r)):
    x1 = cx-r
    x2 = cx+r
    y1 = cy-r
    y2 = cy+r
    subimg = img[y1:y2, x1:x2].copy()
    cv2.circle(subimg,(r,r),r,[255,0,0],2)
    cv2.imshow("subimage", subimg)
    mask = np.zeros(subimg.shape[:2], dtype='uint8')
    cv2.circle(mask,(r,r),r,255,-1)
    subimg = cv2.bitwise_and(subimg, subimg, mask=mask)
    return subimg

file_name = 'parking.jpg'
original_img = cv2.imread (file_name)
print original_img.shape
assert (original_img is not None), 'File not found'
img = original_img.copy()
cv2.imshow("Original", img)		

fr1 = getFrame((150,150,148))
cv2.imshow("frame1", fr1)
fr2 = getFrame((250,150,100))
cv2.imshow("frame2", fr2)

cv2.waitKey(0)
cv2.destroyAllWindows()

