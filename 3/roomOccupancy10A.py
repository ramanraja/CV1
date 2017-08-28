# Motion Detection, post to Dweet; Raspberry PI version; debugged and now Dweeting correctly

# Dweet:
# https://dweet.io/follow/vz-anil-vaidy-raja
# https://freeboard.io/board/OELNmw

# TODO: soft decision (probability of occupation) using logit. 
# Series of probabilities as a time series. Low pass filter the time series to avoid noise.
# This timer will fail if system time is changed/ daylight saving is triggered.

import argparse
import datetime
import my_imutils
import time
import cv2
import json
import dweepy
import warnings

warnings.filterwarnings("ignore")

'''
----------------------------------------------------------------------
# suggested values
blur_neighborhood = 21  # blurring neighbourhood
binary_threshold = 50   # gray scale to binary conversion threshold
resize_width = 500      # width of displayed image frame
min_area = 500          # ignore contours smaller than this in area
alpha_weight = 0.2      # weighted of current frame vis a vis the running avarage
max_idle_time = 120     # seconds before you declare the room to be empty
frame_delay = 10        # millisec between frames
take_snapshots = false  # to take a snapshot every time the occupancy state changes
send_dweet = true       # whether to send status changes to Dweet.io
---------------------------------------------------------------------- 
'''
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--config", default='config.json', help="path to the JSON config file")
ap.add_argument("-v", "--video", required=False, help="path to the input video file")
args = vars(ap.parse_args())

video_file = args["video"]  # can read a camera or a video file 
f = open(args["config"])
conf = json.load(f)
print conf

resize_width = conf["resize_width"]
print 'resize_width: ',resize_width
blur_neighborhood = conf["blur_neighborhood"]
print 'blur_neighborhood: ',blur_neighborhood 
binary_threshold = conf["binary_threshold"]
print 'binary_threshold :', binary_threshold
min_area = conf["min_area"]
print 'contour min_area: ',min_area 
alpha_weight = conf["alpha_weight"]
print 'alpha_weight: ', alpha_weight
max_idle_time = conf["max_idle_time"]
print 'max_idle_time: ',max_idle_time 
frame_delay = conf["frame_delay"]
print 'frame_delay: ', frame_delay
take_snapshots = conf["take_snapshots"]
print 'take_snapshots: ', take_snapshots
send_dweet = conf["send_dweet"]
print 'send_dweet: ', send_dweet
 
def dweet(ts, message):
    print '\n', message, ts
    dweepy.dweet_for('vz-anil-vaidy-raja', {'RMZ CR-7009': message})
    {
        u'content': {u'Conference-Room': u'Status'},
        u'created': ts,
        u'thing': u'Rajaramans RPi Dweeter'
    }

# if the video argument is None, then we are reading from webcam
if video_file is None:
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])
 
text = ["Engaged", "Free"]
font_color = [(0, 0, 255), (0, 255, 0)]    

avg = None
is_free = 1
state_changed = True
deadline = time.time() + max_idle_time
        
# loop over the frames of the video
while True:
    # grab the current frame   
    (grabbed, frame) = camera.read()
     
    # if the frame could not be grabbed, then we have reached the end of the video
    if not grabbed: 
	print "No camera !"
	break
 
    # resize the frame, convert it to grayscale, and blur it
    frame = my_imutils.resize(frame, resize_width)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (blur_neighborhood, blur_neighborhood), 0)
    
    # if average frame is None, initialize it
    if avg is None:
        print "init..",
        avg = gray_img.copy().astype("float")
        continue
        
    # accumulate the weighted average using the current frame and previous frames
    cv2.accumulateWeighted(gray_img, avg, alpha_weight)
        
    # compute the absolute difference between the current frame and running average 
    frameDelta = cv2.absdiff(gray_img, cv2.convertScaleAbs(avg))
    
    # threshold the delta image   (TODO: convert to soft decision)
    thresh = cv2.threshold(frameDelta, binary_threshold, 255, cv2.THRESH_BINARY)[1]
 
    # dilate the thresholded image to fill in holes, then find contours
    thresh = cv2.dilate(thresh, None, iterations=2)
    #(junk_img, cnts, hierarchy) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 
    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < min_area:  
            continue
            
        # Now a significant contour has been found (motion detected):
        # compute the bounding box for the contour, draw it on the frame,
        # and update the status
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # reset timer
        deadline = time.time() + max_idle_time   
        if is_free:  # capture only the edge of the transition
            state_changed = True
        is_free = 0

     
    # if idle wait time is crossed (hysteresis), refresh the running average frame
    if time.time() > deadline:
        avg = None
        deadline = time.time() + max_idle_time  # reset the timer
	if not is_free:  # capture only the edge of the transition
        state_changed = True
	is_free = 1

       
    # draw the text and timestamp on the frame
    cv2.putText(frame, text[is_free], (11, 31), cv2.FONT_HERSHEY_SIMPLEX, 1, [0,0,0], 2)
    cv2.putText(frame, text[is_free], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color[is_free], 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Frame Delta", frameDelta)
    cv2.imshow("Threshold", thresh)
    
    if state_changed:
        state_changed = False
        ts = datetime.datetime.now().strftime("%d-%b-%y, %I_%M_%S_%p")
        if take_snapshots:
            file_name = "captured/Capture_" +ts +".jpg"
            print file_name
            cv2.imwrite(file_name, frame)
        if send_dweet:
            dweet (ts, text[is_free])

    # delay for a few milli seconds before capturing next frame
    key = cv2.waitKey(frame_delay) & 0xFF
    # if the Esc key is pressed, break from the loop
    if key == 27:
        break
         
# cleanup  
camera.release()
cv2.destroyAllWindows()                
