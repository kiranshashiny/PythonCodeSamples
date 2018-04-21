# This loads files from training-data folder and identifies the faces.

#The face detection formulas are in cv2/data folder.
# we use that in the cv2.Cascadeclassifier function.

# next, we pass in the file that we intend to match it.
# this detects that it is a face. and we put rectangles around it.
# python3  load_classifier.py


#$ ls
#__init__.py					haarcascade_fullbody.xml
#__pycache__					haarcascade_lefteye_2splits.xml
#haarcascade_eye.xml				haarcascade_licence_plate_rus_16stages.xml
#haarcascade_eye_tree_eyeglasses.xml		haarcascade_lowerbody.xml
#haarcascade_frontalcatface.xml			haarcascade_profileface.xml
#haarcascade_frontalcatface_extended.xml		haarcascade_righteye_2splits.xml
#haarcascade_frontalface_alt.xml			haarcascade_russian_plate_number.xml
#haarcascade_frontalface_alt2.xml		haarcascade_smile.xml
#haarcascade_frontalface_alt_tree.xml		haarcascade_upperbody.xml
#haarcascade_frontalface_default.xml



import cv2
import numpy as np
import os.path
import matplotlib.pyplot as plt
import time
import glob

def check_file (fname ):
	print ("file name is ", fname)	
	if (os.path.isfile (fname)):
		print ("file is valid")
		return True
	else:
		print ("file is invalid")
		return False

# ONly detects the eye.
#fcascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml')

# This detects the face characteristics.
fcascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

if (fcascade.empty()):
	print ("Yes empty")
else:
        print ("not empty")


files=glob.glob('training-data/*.png')
print (files)

for file in files:
	print (file )
	if (check_file(file)):
		test1 = cv2.imread(file)
	
		gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
	
		cv2.imshow('Test Imag', gray_img)
		#cv2.waitKey(0)
		cv2.destroyAllWindows()
	
		faces = fcascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);
		print ( 'facesfound ', len(faces))
	
		#go over list of faces and draw them as rectangles on original colored img
		for (x, y, w, h) in faces:
	    		cv2.rectangle(test1, (x, y), (x+w, y+h), (255, 255, 0), 2)
	
		# Show the same image in Black and White.
		gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Test Imag', gray_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
		# Show the same image in Color now.
		# black and white - but the BGR2RGB is different.
		gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2RGB)
		cv2.imshow('Test Imag', gray_img)
		cv2.waitKey(0)
		
		cv2.destroyAllWindows()
