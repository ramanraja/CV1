# Mask out a circular piece from a picture; error handling for large radius case 

import numpy as np
import cv2

def getFrame((cx,cy,r)):
    x1 = cx-r
    x2 = cx+r
    y1 = cy-r
    y2 = cy+r
    assert (x1>=0 and x2>=0 and y1>=0 and y2>=0), "Circle spills out of the picture frame: {0},{0},{2}".format (cx,cy,r)
    subimg = img[y1:y2, x1:x2].copy()
    cv2.circle(subimg,(r,r),r,[255,0,0],2)
    #cv2.imshow("subimage", subimg)
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

fr2 = getFrame((250,150,100))
cv2.imshow("frame2", fr2)
# Large radius; goes out of picture boundaries
fr3 = getFrame((100,100,110))
cv2.imshow("frame3", fr3)


cv2.waitKey(0)
cv2.destroyAllWindows()

