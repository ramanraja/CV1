# Load a color image as blak & white with IMREAD_GRAYSCALE flag

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bm.jpg', cv2.IMREAD_COLOR)
cv2.imshow("IMREAD_COLOR", img) 

img2 = cv2.imread('bm.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("IMREAD_GRAYSCALE", img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()
