import cv2, time
from cv2 import VideoCapture

#Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#To capture the video from webcam
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
