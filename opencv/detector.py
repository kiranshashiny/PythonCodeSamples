# Changes - I made recognizer.load -> recognizer-> read ()
# I added the full path to the xml file.
# The trainner.yml isin the current folder.
# Python3 detector.py
# 
import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
#cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print ("Shashi Conf = " ,conf, " Id = ", Id )

        if(conf < 50):
            if ( Id == 1) :
                Id="Anirban"
            elif (Id==4):
                Id="Shashi"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2
        
                cv2.putText(im,'Shashi Kiran!',
        		bottomLeftCornerOfText,
        		font,
        		fontScale,
        		fontColor,
        		lineType)
                
               
            else:
                Id="Unknown"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2

                cv2.putText(im,'Unknown User !',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
