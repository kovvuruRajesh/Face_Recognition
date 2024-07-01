import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import databaseScript
import csv


path = r"C:\Users\pjaga\OneDrive\Desktop\Face_Recognition\Face Recognition\Persons"
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImage = cv2.imread(f"{path}/{cl}")
    images.append(curImage)
    classNames.append(os.path.splitext(cl)[0])


students = classNames.copy()
print(students)

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + ".csv", "w+", newline="")
lnwriter = csv.writer(f)


def findEncodingImg(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img)
        if len(face_locations) == 0:
            encodeList.append(None)
            continue
        encode = face_recognition.face_encodings(img, face_locations)[0]
        encodeList.append(encode)
    return encodeList


databaseScript.create_data()


def check_name_state(name):
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y")
    if not databaseScript.exist_name(name, d1):

        dtstring = now.strftime("%d/%m/%Y %H:%M:%S")
        databaseScript.insert_data(name, dtstring)


known_face_encodings = findEncodingImg(images)
print(known_face_encodings)
print("Encoding complete.....")
# ----------------------------------------------------------------------
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    face_names = []
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        if encodeFace is None:
             continue
        # print("Shape of encodeFace:", encodeFace.shape)
        # print("Shape of known_face_encodings:", known_face_encodings[0].shape)
        matches = face_recognition.compare_faces(known_face_encodings, encodeFace)
        print(matches)
        name = ""
        faceDis = face_recognition.face_distance(known_face_encodings, encodeFace)
        # print(faceDis)
        matcheIndexes = np.argmin(faceDis)
        if matches[matcheIndexes]:
            name = classNames[matcheIndexes]
            print(name)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            face_names.append(name)
            if name in classNames:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

            # check_name_state(name)

    cv2.putText(
        img, "press q to exit", (10, 18), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2
    )
    cv2.imshow("Attendance System", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
