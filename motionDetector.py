import cv2, time, pandas
from datetime import datetime
from cv2 import VideoCapture

#Assigning first_frame to None
first_frame = None

#List when moving object appears
status_list = [None, None]

#Time of movement
times = []

#Initializing DataFrame, one column is start
#Time and other column is end time
df = pandas.DataFrame(columns=["Start", "End"])

#Capturing video
video = cv2.VideoCapture(0)

#Infinite while loop to treat stack of image as video
while True:
    # Reading frame(image) from video
    check, frame = video.read()
    #Initializing motion = 0(No motion)
    status = 0
    # Converting color image to gray_scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Converting gray scale image to gaussian blur image, so that change can be find easily
    gray = cv2.GaussianBlur(gray, (21,21), 0)

#This is used to store the first image/frame of the video
    # In first iteration we assign the value
    # of static_back to our first frame
    if first_frame is None:
        first_frame = gray
        continue
# Calculates the difference between first frame and other frames
# Difference between static background
    # and current frame(which is GaussianBlur)
diff_frame = cv2.absdiff(first_frame, gray)

#Provides a threshold value, such that it will convert the difference value with less than 30 to black.
#If the difference is greater than 30 it will convert those pixels to white
thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

#Define the contour area.Basically, add the borders
(cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#For removing noises and shadows. Basically, it will keep only that part white, which has area greater than 1000 pixels
for contour in cnts:
    if cv2.contourArea(contour)<10000:
        continue
    status = 1

    (x, y, w, h) = cv2.boundingRect(contour)
    # making green rectangle around the moving object
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

# Appending status of motion
status_list.append(status)

status_list = status_list[-2:]

# Appending Start time of motion
if status_list[-1] == 1 and status_list[-2] == 0:
    times.append(datetime.now())
# Appending End time of motion
if status_list[-1] == 0 and status_list[-2] == 1:
    times.append(datetime.now())

cv2.imshow("Gray Frame",gray)
cv2.imshow("Delta Frame",diff_frame)
cv2.imshow("Threshold Frame",thresh_frame)
cv2.imshow("Color Frame",frame)

key = cv2.waitKey(1)


if key == ord('q'):
    if status == 1:
        times.append(datetime.now())


print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()







