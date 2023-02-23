import face_recognition
import cv2
import os
import numpy as np
from text_to_speech import *
import RPi.GPIO as GPIO

# TODO
# TTS for multiple faces, GPIO

GPIO.setmode(GPIO.BCM)
#Setting GPIO pin numbers for speak and quit buttons
speak_button = 14
quit_button = 15

#Setting button GPIO pins as inputs for both buttons and enables internal pull down resistors
GPIO.setup(speak_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(quit_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

video_capture = cv2.VideoCapture(0)

folder_dir = "/home/pi/code/sciencefair22-23/nemo/images"

known_face_encodings = []
known_face_names = []

for image in os.listdir(folder_dir):
    face = face_recognition.load_image_file("images/"+image)
    
    known_face_encodings.append(face_recognition.face_encodings(face)[0])
    known_face_names.append(os.path.splitext(image)[0].capitalize())

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    speak_button_state = GPIO.input(speak_button)
    quit_button_state = GPIO.input(quit_button)
    
    ret, frame = video_capture.read()
    
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        rgb_small_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)
            
            #On speak_button or s key press
            #TODO: Check if state needs to be 1 or 0
            if ((speak_button_state==1) or (cv2.waitKey(1) & 0xFF == ord('s'))):
                speak(name)

    process_this_frame = not process_this_frame
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    cv2.imshow('Video', frame)
    
    #On quit_button press
    if ((quit_button_state==1) or (cv2.waitKey(1) & 0xFF == ord('q'))):
        break
    
video_capture.release()
cv2.destroyAllWindows()
GPIO.cleanup()