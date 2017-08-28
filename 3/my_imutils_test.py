# test cases for my_imutils

import cv2
import numpy as np
import my_imutils

lis = my_imutils.list_files(".")
print lis
print '-'*20
lis = my_imutils.list_files("..\image4", '*.jpg')
print lis
print '-'*20
file_name = 'jurassic.jpg'
img = cv2.imread(file_name)
img2 = my_imutils.resize(img, 200)
cv2.imshow("Resized", img2) 
cv2.waitKey(0)
cv2.destroyAllWindows()    