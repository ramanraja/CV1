# Split the channels using numpy and show R,G,B separately

import cv2
import numpy as np

img = cv2.imread("smallcars.jpg")
cv2.imshow("Original", img)
print img.shape

# black = np.zeros(img.shape, dtype='uint8')  # wrong: it must be 2 dimensional
black = np.zeros(img.shape[0:2], dtype='uint8') 
b,g,r = cv2.split(img)

comb1 = cv2.merge((b,black,black))   
cv2.imshow("Blue", comb1)

comb2 = cv2.merge((black,g,black))   
cv2.imshow("Green", comb2)

comb3 = cv2.merge((black,black,r))  
cv2.imshow("Red", comb3)

cv2.waitKey(0)
cv2.destroyAllWindows()




