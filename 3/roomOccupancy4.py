# Motion Detection with weighted average of previous frames and hysteresis
# http://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/

import argparse
import datetime
import my_imutils
import time
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
blur = 21 
the_threshold = 50       
resize_width = 500 
min_area = args["min_area"]
alpha_weight = 0.2  
motion_detected = False
 
# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)
# otherwise, we are reading from a video file
else:
	camera = cv2.VideoCapture(args["video"])
 
# initialize the first frame in the video stream

avg = None
idle_time_counter = 0
max_idle_time = 10 # 'seconds' before you declare the room to be empty
frame_delay = 10   # millisec between frames
max_idle_count = int(1000.0/frame_delay * max_idle_time)
is_free = 1
text = ["Occupied", "Free"]
font_color = [(0, 0, 255), (0, 255, 0)]	

print 'frame_delay: ', frame_delay
print 'max_idle_count:', max_idle_count
			
# loop over the frames of the video
while True:
	# grab the current frame   
	(grabbed, frame) = camera.read()
     
	# if the frame could not be grabbed, then we have reached the end of the video
	if not grabbed: break
 
	# resize the frame, convert it to grayscale, and blur it
	frame = my_imutils.resize(frame, resize_width)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (blur, blur), 0)
	
	# if average frame is None, initialize it
	if avg is None:
		print "initializing idle scene..."
		avg = gray.copy().astype("float")
		continue
		
	# accumulate the weighted average between the current frame and previous frames
	cv2.accumulateWeighted(gray, avg, alpha_weight)
		
	# compute the absolute difference between the current frame and running average 
	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
	
	# threshold the delta image
	thresh = cv2.threshold(frameDelta, the_threshold, 255, cv2.THRESH_BINARY)[1]
 
	# dilate the thresholded image to fill in holes, then find contours
	thresh = cv2.dilate(thresh, None, iterations=2)
	(junk_img, cnts, hierarchy) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < min_area:
			continue
 
		# compute the bounding box for the contour, draw it on the frame,
		# and update the status
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		is_free = 0
		
	# draw the text and timestamp on the frame
	cv2.putText(frame, text[is_free], (11, 31), cv2.FONT_HERSHEY_SIMPLEX, 1, [0,0,0], 2)
	cv2.putText(frame, text[is_free], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color[is_free], 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
 
	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Threshold", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(frame_delay) & 0xFF
	
	# reset the hysteresis for idle time
	idle_time_counter = (idle_time_counter+1) % max_idle_count
	if idle_time_counter==0:
	   is_free = 1
	   avg = None
	
	# if the Esc key is pressed, break from the loop
	if key == 27:
		break
		 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()				