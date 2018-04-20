import numpy as np
import cv2 

#Get the Training data first.

face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

eye_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

img = cv2.imread('sachin.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if ( len( gray) ==0 ):
	print ("image is empty")
else :
	print ("Image is good")

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#
#for (x,y,w,h) in faces:
#    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#    roi_gray = gray[y:y+h, x:x+w]
#    roi_color = img[y:y+h, x:x+w]
#    eyes = eye_cascade.detectMultiScale(roi_gray)
#    for (ex,ey,ew,eh) in eyes:
#        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#cv.imshow('img',img)
#cv.waitKey(0)
#cv.destroyAllWindows()
