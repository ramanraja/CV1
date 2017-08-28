# Motion Detection;post to Dweet;Network auto-reset; LEDs and 3 buttons; Headless operation

# Dweet:
# https://dweet.io/follow/vz-anil-vaidy-raja
# https://freeboard.io/board/OELNmw

# TODO: 
# Make the code object oriented & multi threaded
# Relay control
# Third button to reset network interface
# make the display optional; make fps and resolution configurable
# soft decision (probability of occupation) using logit. 
# Use audio detection and motion detection PIR sensor. Take majority logic/probabilistic combination.
# Series of probabilities as a time series. Low pass filter the time series to avoid noise.

'''
#--------------------------------------------------------------------------------
# suggested values
network_interface = "wlan0"  # network interface can be eth0, wlan0 or usb0
blur_neighborhood = 21       # blurring neighbourhood
binary_threshold = 50        # gray scale to binary conversion threshold
resize_width = 500           # width of displayed image frame
min_area = 500               # ignore contours smaller than this in area
alpha_weight = 0.2           # weighted of current frame vis a vis the running avarage
max_idle_time = 120          # seconds before you declare the room to be empty
frame_delay = 10             # millisec between frames
resolution = [640,480]       # camera resolution
fps = 16                     # frames per second
take_snapshots = false       # to take a snapshot every time the occupancy state changes
send_dweet = true            # whether to send status changes to Dweet.io
display_fame = ture               # whether to show the frame on the screen
auto_shutdown = true         # whether to automatically shutdown the Raspberry Pi
#--------------------------------------------------------------------------------
'''

import argparse
import datetime
import my_imutils
import time
import cv2
import json
import dweepy
import os
import warnings
import sys
from requests.exceptions import ConnectionError
from subprocess import call
from subprocess import Popen, PIPE
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera

#--------------------------------------------------------------------------------
def process_button1():
    print 'Button 1 pressed'
    count = 0
    for i in range(5):
        time.sleep(0.02)   # 20 mSec
        if(GPIO.input(button1)==0): count+=1
    if (count>2):
	return CHECK_NET
    else:
        return BUTTON_NOISE

#--------------------------------------------------------------------------------
def process_button3():
    print 'Button 3 pressed'
    set_led(red_led, OFF)
    set_led(green_led, OFF)
    count = 0
    for i in range(40):
        set_led(blue_led, ON)
        time.sleep(0.05)   # 50 mSec
        set_led(blue_led, OFF)
        time.sleep(0.05)   # 50 mSec
        if(GPIO.input(button3)==0): count+=1
    set_led(blue_led, OFF)
    set_led(STATE_LED[is_free], ON)
    set_led(STATE_LED[~is_free], OFF)
    if (count>29):
        return TERMINATE
    else:
        return BUTTON_NOISE

#--------------------------------------------------------------------------------
def process_button2():
    print 'Button 2 pressed'
    count = 0
    for i in range(7):
        time.sleep(0.02)   # 20 mSec
        if(GPIO.input(button2)==0): count+=1
    if (count>4):
	return RESET_NET
    else:
        return BUTTON_NOISE
#--------------------------------------------------------------------------------

def shutdown_pi():
    print "Shutting Down !!!............"
    command = "/usr/bin/sudo /sbin/shutdown now"      # fully shutdown
    #command = "/usr/bin/sudo /sbin/shutdown -r now"  # -r will restart
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
#--------------------------------------------------------------------------------
def check_network():   
    set_led (blue_led, ON)
    set_led (green_led, OFF)
    set_led (red_led, OFF)

    p = Popen(['hostname', '-I'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode
    message = "dummy.."
    if (rc==0):
	message = output.strip()
    ts = datetime.datetime.now().strftime("%d-%b-%y, %I_%M_%S_%p")
    if (dweet (ts, message)):
        set_led (blue_led, OFF)
	flash_led (green_led, 8,150)
    else:
        set_led (blue_led, OFF)
	flash_led (red_led, 8,150)
        print 'Trying to start DHCP...'
        rc = call (["sudo", "dhclient", network_interface])
        print "Return code:", rc
    set_led(STATE_LED[is_free], ON)
    set_led(STATE_LED[~is_free], OFF)
    dweet (ts, text[is_free])
#--------------------------------------------------------------------------------
def reset_network():
    set_led (blue_led, ON)
    set_led (green_led, OFF)
    set_led (red_led, OFF)

    print 'Resetting network interface...'
    rc = call (["sudo", "/etc/init.d/networking", "restart"])
    print "Return code:", rc
    flash_led (blue_led, 10,100)   

    set_led(STATE_LED[is_free], ON)
    set_led(STATE_LED[~is_free], OFF)
    dweet (ts, text[is_free])
#--------------------------------------------------------------------------------
def set_led (led, on_off):
    GPIO.output(led, on_off)
#--------------------------------------------------------------------------------

def flash_led (led, times=1, on_msec=100, off_msec=None):
    if off_msec is None: 
	off_msec = on_msec
    ontime = 0.001*on_msec
    offtime = 0.001*off_msec
    for i in range(times):
	GPIO.output(led, GPIO.HIGH)
	time.sleep(ontime)
	GPIO.output(led, GPIO.LOW)
	time.sleep(offtime)
#--------------------------------------------------------------------------------

def dweet(ts, message):
    print '\n', message, ts
    try:
	dweepy.dweet_for('vz-anil-vaidy-raja', {'RMZ CR-7009': message})
	{
	u'content': {u'Conference-Room': u'Status'},
	u'created': ts,
	u'thing': u'Rajaramans RPi Dweeter'
	}
    	return True
    except ConnectionError:
	print "No network connection"
	# the following line woks well for usb0, but hangs wlan0
        if (network_interface=='usb0'):
            rc = call (["sudo", "dhclient", network_interface]) # self-healing network ?!
            print "Return code:", rc
        return False
#--------------------------------------------------------------------------------

warnings.filterwarnings("ignore")

GPIO.setmode(GPIO.BCM)  # NOTE: GPIO pins are specified

red_led = 14    # connector pin 8
blue_led = 15     # pin 10
green_led = 18      # pin 12

button1 = 25  # pin 22
button2 = 24  # pin 18
button3 = 23  # pin 16

GPIO.setup(blue_led,  GPIO.OUT)
GPIO.setup(red_led,   GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

ON = GPIO.HIGH
OFF = GPIO.LOW
STATE_LED = [red_led, green_led]

set_led(red_led, OFF)
set_led(green_led, OFF)
flash_led (blue_led,8,200)
set_led(blue_led, OFF)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--config", default='/home/pi/cv1/config.json', help="path to the JSON config file")
ap.add_argument("-v", "--video", required=False, help="path to the input video file")
args = vars(ap.parse_args())

home_dir = "/home/pi/cv1/"
print 'Changing to home directory: ', home_dir
os.chdir(home_dir)
myc = call (["pwd"])

video_file = args["video"]  # can read a camera or a video file 
f = open(args["config"])
conf = json.load(f)
print conf

print args["config"]
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
display_fame = conf["display_fame"]
print 'display_fame: ', display_fame
take_snapshots = conf["take_snapshots"]
print 'take_snapshots: ', take_snapshots
send_dweet = conf["send_dweet"]
print 'send_dweet: ', send_dweet 

network_interface = conf["network_interface"]
print 'network_interface: ', network_interface
resolution = conf["resolution"]
print 'resolution: ', resolution
fps = conf["fps"]
print 'fps: ', fps
auto_shutdown = conf["auto_shutdown"]
print 'auto_shutdown: ', auto_shutdown

text = ["Engaged", "Free"]
font_color = [(0, 0, 255), (0, 255, 0)]    

CHECK_NET = 5
RESET_NET = 7
TERMINATE = 9
BUTTON_NOISE = 11

command = CHECK_NET
button_spikes = 0
avg = None
is_free = 1
state_changed = True
deadline = time.time() + max_idle_time

warmup_time = 2.5
# Use the PiCamera, not USB camera
camera = PiCamera()
camera.resolution = resolution
camera.framerate = fps
#camera.rotation = 180
imgarray = PiRGBArray(camera, size=tuple(resolution))
print "Warming up..."
time.sleep(warmup_time)
     
try:   
	# loop over the frames of the video
	for f in camera.capture_continuous(imgarray, format="bgr", use_video_port=True):
	    # grab the current frame   
	    frame = f.array
	     
	    # if the frame could not be grabbed, then we have reached the end of the video
	    #if not grabbed: 
		#print "No camera !"
		#break
	 
	    # resize the frame, convert it to grayscale, and blur it
	    frame = my_imutils.resize(frame, resize_width)
	    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    gray_img = cv2.GaussianBlur(gray_img, (blur_neighborhood, blur_neighborhood), 0)
	    
	    # if average frame is None, initialize it
	    if avg is None:
	        sys.stdout.write ("init..")
	        sys.stdout.flush()
	        avg = gray_img.copy().astype("float")
	        imgarray.truncate(0)  # without this, 'incorrect buffer length' error will appear
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
	    if display_fame:
	        cv2.putText(frame, text[is_free], (11, 31), cv2.FONT_HERSHEY_SIMPLEX, 1, [0,0,0], 2)
	        cv2.putText(frame, text[is_free], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color[is_free], 2)
	        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
	                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
	        cv2.imshow("Security Feed", frame)
	        #cv2.imshow("Frame Delta", frameDelta)
	        cv2.imshow("Threshold", thresh)
	
	    if state_changed:
	        state_changed = False
		set_led(STATE_LED[is_free], ON)
	        set_led(STATE_LED[~is_free], OFF)
	        ts = datetime.datetime.now().strftime("%d-%b-%y, %I_%M_%S_%p")
	        if take_snapshots:
	            file_name = "captured/Capture_" +ts +".jpg"
	            print file_name
	            cv2.imwrite(file_name, frame)
	        if send_dweet:
	            dweet (ts, text[is_free])
	
	    # read the buttons and take action
	    if(GPIO.input(button1)==0):
	    	command = process_button1()
	    	if (command == CHECK_NET):
		    check_network()
	    	else:
	            button_spikes += 1
	
	    if(GPIO.input(button2)==0):
	    	command = process_button2()
	    	if (command == RESET_NET):
	 	    reset_network()
	    	else:
	            button_spikes += 1
	
	    if(GPIO.input(button3)==0):
	    	command = process_button3()
	    	if (command == TERMINATE):
	 	    break
	    	else:
	            button_spikes += 1
	
	    imgarray.truncate(0)  # without this, 'incorrect buffer length' error will appear
	
	    # delay for a few milli seconds before capturing next frame
	    key = cv2.waitKey(frame_delay) & 0xFF
	    # if the Esc key is pressed, break from the loop
	    if key == 27:
        	break
except KeyboardInterrupt:
	print "Keyboard interrupt"
         
# cleanup  
#camera.release()
GPIO.cleanup()
# TODO: terminate worker threads
cv2.destroyAllWindows()      
          
print "\nThere were ", button_spikes, "button noise spikes"
if (auto_shutdown and command==TERMINATE):
    shutdown_pi()
else:
    print "Bye !....."
	










