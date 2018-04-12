import cognitive_face as CF
import time
import picamera
import RPi.GPIO as GPIO
import requests
import sonar
import faceDetect

faceDetect.setup()
#Sets up board for reading in the from the camera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
camera = picamera.PiCamera()

#Sets up paths
requests.packages.urllib3.disable_warnings()
face = 'FaceSensor/face'
count = 1

while True:
    distance = sonar.sonar()
    if(distance > 90):
        print("No intruders")
        time.sleep(1)
    else:      
        if(count < 10):   
            locFace = face + '0000' + str(count)  #When output from motion sensor is HIGH
        elif(count> 10):
            locFace = face + '000' + str(count)
        elif (count > 10 and count < 100):
            locFace = face + '00' + str(count)
        elif(count>100 and count < 1000):
            locFace = face + '0' + str(count)
        else:
            locFace = face + str(count)

        count = count + 1
        locFace = locFace + '.jpg'
        print("Intruder detected")
        camera.capture(locFace)
        faceDetect.auth(locFace)
        time.sleep(5)
     




