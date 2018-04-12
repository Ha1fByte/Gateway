import json
import requests
import cognitive_face as CF

def setup():
  key = ''  # Replace with a valid Subscription Key here.
  CF.Key.set(key)
  base_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
  CF.BaseUrl.set(base_url)
  
  headers = {'Content-Type': 'application/octet-stream',
             'Ocp-Apim-Subscription-Key': key}
  url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'
  params = {
      'returnFaceId': 'true',
      'returnFaceAttributes':'emotion',
      #'returnFaceLandmarks' : 'true',
}

def auth(face):
  # Gets the binary file data so we can send it to MCS
  
  data = open(face, 'rb')
  response = requests.post(url, headers=headers, data=data, params=params)
  
  data = open('Trevor.jpg', 'rb')
  response2 = requests.post(url, headers=headers, data=data, params=params)
  
  parsed = response.json()
  #print(parsed)
  
  requests.packages.urllib3.disable_warnings()
  json_data = json.loads(response.text)
  json_data2 = json.loads(response2.text)
  # = CF.face_list.create(face_list_id='0120', name='natalie', user_data=json_data2[0]['faceId'])
  #CF.face_list.add_face(image='natalie.jpg', face_list_id='0120')
  #group = CF.face_list.get('0120')
  similarity = CF.face.verify(json_data[0]['faceId'], json_data2[0]['faceId'])
  print(similarity.get('isIdentical'))
  print("%" + str(similarity.get('confidence')*100))

