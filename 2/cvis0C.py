# Display two images side by side (?!!)

import cv2

img = cv2.imread('photo.png', cv2.IMREAD_GRAYSCALE)
print img.shape
img2 = cv2.hconcat(img, img) # I meant to use np.hstack !
cv2.imshow("Pictures", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


