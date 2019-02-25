import cv2
import face_recognition
import pymysql
import datetime
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="Akarsh@97",
  database="face"
)
input_movie = cv2.VideoCapture(0)
akarsh = face_recognition.load_image_file("img.jpg")
manjit = face_recognition.load_image_file("img1.jpg")
suresh = face_recognition.load_image_file("img2.jpg")
face_encoding = face_recognition.face_encodings(akarsh)[0]
face_encoding0 = face_recognition.face_encodings(manjit)[0]
face_encoding1 = face_recognition.face_encodings(suresh)[0]
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output1.avi', fourcc, 10, (640,480)) 
known_faces = [
face_encoding ,face_encoding0, face_encoding1
]
# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
c=0
sql = "select * from facereco"
mycursor = mydb.cursor()
b = mycursor.execute(sql)
row = mycursor.fetchone()
if row == None:
     sql = "INSERT INTO facereco (Name) VALUES(' ')";
     mycursor.execute(sql)
     mydb.commit()
          

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1
    frameRate = 0.5
    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
        print(match)
        name = None
        mydt = datetime.datetime.now().date()
        
            
        if match[0]:
            name = "Akarsh"
            sql = "select * from facereco where name = '"+name+"' and date(DT) !=  " + str(mydt)
            mycursor = mydb.cursor()
            b = mycursor.execute(sql)
            row1 = mycursor.fetchone()
            if row1 == None:
                sql = "INSERT INTO facereco (Name) VALUES('"+name+"')";
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                face_names.append(name)
            else:
                print("Attendence already taken")
        if match[1]:
            name = "Manjit"
            sql = "select * from facereco where name = '"+name+"' and date(DT) !=  " + str(mydt)
            mycursor = mydb.cursor()
            b = mycursor.execute(sql)
            row1 = mycursor.fetchone()
            if row1 == None:
                sql = "INSERT INTO facereco (Name) VALUES('"+name+"')";
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                face_names.append(name)
            else:
                print("Attendence already taken")
        if match[2]:
            name = "Suresh"
            sql = "select * from facereco where name = '"+name+"' and date(DT) !=  " + str(mydt)
            mycursor = mydb.cursor()
            b = mycursor.execute(sql)
            row1 = mycursor.fetchone()
            if row1 == None:
                sql = "INSERT INTO facereco (Name) VALUES('"+name+"')";
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                face_names.append(name)
            else:
                print("Attendence already taken")

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue
        
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video', frame)
    out.write(frame)
    # Write the resulting image to the output video file
# All done!
input_movie.release()
cv2.destroyAllWindows()
