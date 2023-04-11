import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Faces
img = face_recognition.load_image_file("data/Ranjeetsingh.jpg")
img_encoding = face_recognition.face_encodings(img)[0]

known_face_encodings = [img_encoding]
known_face_name = ["Ranjeet"]

# list of Expected Students
students = known_face_name.copy()

face_locations = []
face_encodings = []

# Get the current Data and Time

now = datetime.now()
current_data = now.strftime("%Y-%m-%d")

f = open(f"{current_data}.csv", "w+",newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0), fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    
    # Recognize Faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if(matches[best_match_index]):
            name = known_face_name[best_match_index]
            
        # Add the text if a person is present
        if name in known_face_name:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (225,0,0)
            thickness = 3
            LineType = 2
            cv2.putText(frame,name + "Present",bottomLeftCornerOfText,fontScale,fontColor,
                        thickness,LineType)
            
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M%S")
                lnwriter.writerow([name,current_time])
                
            
    cv2.imshow("Attendace",frame)
    if cv2.waitkey(1) & 0xFF == ord("q"):
        break
    
video_capture.release()
cv2.destroyAllWindows()
