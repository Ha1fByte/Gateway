import cognitive_face as CF
import time
import picamera
import RPi.GPIO as GPIO
import requests

import sonar

key = ''  # Replace with a valid Subscription Key here.
CF.Key.set(key)
base_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(base_url)

#Sets up board for reading in the from the camera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
camera = picamera.PiCamera()

#Sets up paths
requests.packages.urllib3.disable_warnings()
face = 'FaceSensor/face'
count = 1
params = {
    'returnFaceId': 'true',
    'returnFaceAttributes':'emotion',
    #'returnFaceLandmarks' : 'true',
}
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': key}

url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'



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
        time.sleep(10)
        #data = open(locFace, 'rb')
        #response = requests.post(url, headers=headers, data=data, params=params)
        #similarity = CF.face.verify(face, defaultFace)
        #if (similarity.get('isIdentical')):
        #    print("Hello Natalie")
        #else:
        #    print("Unauthorized Personal")


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

