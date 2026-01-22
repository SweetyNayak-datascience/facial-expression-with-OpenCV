import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from default camera (0)
video_cap = cv2.VideoCapture(0)

while True:
    ret, frame = video_cap.read()
    if not ret:
        break  # If frame not read properly, exit loop

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Resize and save the face region
        resized_face = cv2.resize(roi_color, (200, 200))

        # Save the face as an image file
        cv2.imwrite("detected_face.jpg", resized_face)

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the frame with rectangle(s)
    cv2.imshow('Face Detection', frame)

    # Exit loop if 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video_cap.release()
cv2.destroyAllWindows()
