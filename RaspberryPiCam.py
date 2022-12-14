from picamera import PiCamera
import time
from time import sleep
import io
import cv2
import numpy

"""
Project Goal: face tracking with PiCamera

Installations:
    sudo apt-get install python-opencv
    sudo apt-get install python-picamera
"""

""" ============== documentation ================= """
""" image effects:
camera.image_effect = ""

none
negative
solarize
sketch
denoise
emboss
oilpaint
hatch
gpen
pastel
watercolor
film
blur
saturation
colorswap
washedout
posterise
colorpoint
colorbalance
cartoon
deinterlace1
deinterlace2

Exposure options:
camera.exposure_mode = ""

off
auto
night
nightpreview
backlight
spotlight
sports
snow
beach
verylong
fixedfps
antishake
fireworks

White Balance: 
camera.awb_mode = ""

off
auto
sunlight
cloudy
shade
tungsten
fluorescent
incandescent
flash
horizon

"""

camera = PiCamera()
camera.start_preview(alpha = 200) # get live feed
camera.brightness = 70
# camera.resolution = (2592, 1944) # images resolution
camera.vflip = True
camera.rotation = 0 # images are upright

for i in range (1): # capture i images
    sleep(2)
    camera.capture('/home/pi/Desktop/photo%s.jpg' % i)
    camera.annotate_text_size = 20
    camera.annotate_text = "Hello World!"

"""
# camera.resolution = (1920, 1080)
camera.framerate = 15
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(2) # length of video
camera.stop_recording()
"""

camera.stop_preview()

""" ================== facial detection ======================

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
cv2.imwrite('result.jpg',image)

"""