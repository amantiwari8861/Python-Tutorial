#pip install mysql-connector-python
#pip install opencv-python 
#pip install face-recognition


# pip install dlib --verbose --global-option=build_ext --global-option="-LC:\temp\openblash\bin" --global-option="-IC:\temp\openblash\include" --global-option="-DCMAKE_LIBRARY_PATH=C:\temp\openblash\bin"

import cv2
import face_recognition
import mysql.connector

def face_recognition_login():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
       host='localhost',
        user='root',
        password='1234',
        database='pdbc'
    )
    cursor = connection.cursor()

    # Start video capture
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) == 1:
            # Only proceed if exactly one face is detected
            face_encoded = face_recognition.face_encodings(frame, face_locations)[0]

            # Retrieve all faces from the database and compare with the captured face
            cursor.execute("SELECT username, face_data FROM user_faces")
            for username, face_data in cursor:
                stored_face_encoded = face_data  # The data is already stored as bytes in the database.
                stored_face = face_recognition.face_encodings([stored_face_encoded])[0]
                match = face_recognition.compare_faces([stored_face], face_encoded)

                if match[0]:
                    print(f"Welcome, {username}!")
                    break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and destroy windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition_login()
