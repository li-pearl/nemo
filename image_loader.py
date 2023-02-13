# # NONE OF THIS WORKS

# import face_recognition
# import cv2
# import numpy as np

# # TODO
# # Add descriptions to each person
# # Make it work :/

# class Face:
#     def __init__(self, name, image):
#         self.name = name
#         self.image = face_recognition.load_image_file(image)
#         self.face_encoding = face_recognition.face_encodings(image)[0]
        
#     def get_name(self):
#         return self.name
        
#     def get_face_encoding(self):
#         return self.face_encoding

# # Input known people's names and faces
# # Find way to input images
# anirbanFace = Face("Anirban", "images/anirban.jpg")
# shilpiFace = Face("Shilpi", "images/shilpi.jpg")
# borshuenFace = Face("Bor-Shuen", "images/borshuen.jpg")
# dhananjayFace = Face("Dhananjay", "images/dhananjay.jpg")
# jaysonFace = Face("Jason", "images/jayson.jpg")
# anshiFace = Face("Anshi", "images/anshi.jpg")
# aineshFace = Face("Ainesh", "images/ainesh.jpg")
# astridFace = Face("Astrid", "images/astrid.jpg")

# known_faces = [
#     anirbanFace,
#     shilpiFace,
#     borshuenFace,
#     dhananjayFace,
#     jaysonFace,
#     anshiFace,
#     aineshFace,
#     astridFace
# ]

# # Generates a list of known face encodings
# known_face_encodings = []

# for face in known_faces:
#     known_face_encodings.append(face.get_face_encoding)
    
# # Generates a list of known face names    
# known_face_names = []

# for face in known_faces:
#     known_face_names.append(face.get_name)