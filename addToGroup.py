import json
import requests
import cognitive_face as CF

def add(image, group):
    CF.face_list.add_face(image=image, face_list_id=group)

def imagine_rit_add(image):
    CF.face_list.add_face(image= image, face_list_id='69')

def initilize():
    CF.face_list.create(face_list_id='69', name='imagine', user_data='Group of approved people')


