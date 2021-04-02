#import faceee
import face_recognition
import cv2
import os
#from pymongo import MongoClient

video_capture = cv2.VideoCapture(0)

finalName = ""
# Load images.

image_1 = face_recognition.load_image_file("C:\\Users\\Shrijith\\Desktop\\sihh\\5.jpg")
image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
image_5 = face_recognition.load_image_file("C:\\Users\\Shrijith\\Desktop\\sihh\\babu.jpg")
image_5_face_encoding = face_recognition.face_encodings(image_5)[0]

image_7 = face_recognition.load_image_file("C:\\Users\\Shrijith\\Desktop\\sihh\\jason.jpg")
image_7_face_encoding = face_recognition.face_encodings(image_7)[0]

image_3 = face_recognition.load_image_file("C:\\Users\\Shrijith\\Desktop\\sihh\\Shrijith.jpg")
image_3_face_encoding = face_recognition.face_encodings(image_3)[0]
image_4 = face_recognition.load_image_file("C:\\Users\\Shrijith\\Desktop\\sihh\\will.jpg")
image_4_face_encoding = face_recognition.face_encodings(image_4)[0]

known_face_encodings = [

    image_1_face_encoding,
    image_5_face_encoding,
    image_7_face_encoding,
    image_3_face_encoding,
    image_4_face_encoding

]
known_face_names = [

    "Srk",
    "yogi babu",
    "jason",
    "Shrijith",
    "smith"

]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
current_path = os.getcwd()

while True:

    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # BGR to RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        face_names.append(name)
        process_this_frame = not process_this_frame
    counter=0
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        # label
        if (name=="Shrijith"):
            finalName = name
            crop_img = frame[(top-30):(bottom), (left):(right)]
            cv2.imwrite("C:\\Users\\Shrijith\\Desktop\\sihh"+"/yola/"+ "imagelol" + ".png", crop_img)
            counter = counter + 1
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        print((left, top), (right, bottom))
        finalName = name
    # Display
    cv2.imshow('Video', frame)

    # quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# kill process
video_capture.release()
cv2.destroyAllWindows()

'''
conn = MongoClient("mongodb+srv://newuser:newuser@cluster0-c1dqn.mongodb.net/test?retryWrites=true&w=majority", 27017)
print("Connected successfully!!!")

#print("Could not connect to MongoDB")

# database
db = conn.test
#name1 = "Shrijith"


collection = db.employees

result = collection.find()

for i in result:
    if(i["name"] == finalName):
        collection.update_one({'_id' : i["_id"]},
                               {
                                   "$set":{
                                       "emotionScore": faceee.score
                                   }
                               })

        break

