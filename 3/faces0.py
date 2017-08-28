# Face detection with Harr classifier
# http://fideloper.com/facial-detection
 
import cv2

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

rects, img = detect("bm.jpg")
for x1, y1, x2, y2 in rects:
     cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



















