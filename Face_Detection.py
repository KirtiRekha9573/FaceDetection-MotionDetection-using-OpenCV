import cv2

#Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Reading the image as it is
img = cv2.imread("C://Users//CSUFTitan//Documents//Languages//FaceDetectorandMotionDectectorUsingOpenCV//deepika.jpg", 1)

#Reading the image as it is
#img = cv2.imread("I.jpeg")

#Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img =cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

#Resizing the image
resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
#Displaying the image
cv2.imshow("Kirti", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()
