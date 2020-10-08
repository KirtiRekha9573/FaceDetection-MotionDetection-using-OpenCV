import cv2

#Colored Image
img = cv2.imread("C://Users//CSUFTitan//Documents//Languages//FaceDetectorandMotionDectectorUsingOpenCV//deepika.jpg", 1)

#For gray-scaled image
#img = cv2.imread("C://Users//CSUFTitan//Documents//Languages//FaceDetectorandMotionDectectorUsingOpenCV//penguin.jpg", 0)

#To know image is stored in which format
print(type(img))
print(img)

#To know shape of the image, use shape function --> Gray scale- 408 rows, 612 columns. Colored image 408 rows, 612 columns, 3 channels -RGB
print(img.shape)

#To resize the image
resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

#Displaying the image
cv2.imshow("Kirti", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()

