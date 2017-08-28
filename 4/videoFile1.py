import cv2

#camera = cv2.VideoCapture("C:/Users/Raja/PythonWD/CV/pictures3/movie.mp4")
#camera = cv2.VideoCapture("C:/Users/Raja/PythonWD/CV/pictures3/yoga.flv")
#camera = cv2.VideoCapture("C:\\Users\\Raja\\PythonWD\\CV\\pictures3\\yoga.flv")
#camera = cv2.VideoCapture("C:/Users/Raja/PythonWD/CV/pictures3/akshay.MOV")
camera = cv2.VideoCapture("akshay.MOV")
print camera
flag,frame = camera.read()
print flag
cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
