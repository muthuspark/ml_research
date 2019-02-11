import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('/home/wolf/haars/output/cascade.xml')
img = cv.imread('resources/Sudoku16.jpg')
height, width = img.shape[:2]
img = cv.resize(img,(np.int_(0.5*width), np.int_(0.5*height)), interpolation = cv.INTER_CUBIC)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()
