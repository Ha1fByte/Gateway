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
     


img_urls = [
    'https://www.barnett-waddingham.co.uk/media/thumbnail/ca/ca/cacac3935e9b2cf046c0db71729ed1b8/jade-taylor.jpg',
    'https://st2.depositphotos.com/3752845/8411/i/950/depositphotos_84116536-stock-photo-jade-taylor-actress.jpg']

#faces = [CF.face.detect(img_url) for img_url in img_urls]

# Assume that each URL has at least one face, and that you're comparing the first face in each URL
# If not, adjust the indices accordingly.
#similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])
#print(similarity.get('isIdentical'))
#if(similarity.get('isIdentical')):
#    print('Hello Authorized user')
#else:
#    print('Unauthorized User')

