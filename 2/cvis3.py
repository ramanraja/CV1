# take the file name from command line
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])

print "height: %d pixels" % (img.shape[0])
print "width: %d pixels"  % (img.shape[1])
print "channels: %d"   % (img.shape[2])

print img.size       # number of pixes
print img.shape      # height, width

print img.shape[0] * img.shape[1] * img.shape[2]

cv2.imshow("The Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()