

BGR-> Gray and
BGR -> HSV are the most popular 2 colors that can convert images from one to another.

Simple Code to check if the image could be converted or not.

	img = cv2.imread('trump.png')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if ( len( gray) ==0 ):
		print ("image is empty")
	else :
		print ("Image is good")

The different FaceRecognizers used for recognizing images are:

	createEigenFaceRecognizer(...)
	recognizer = cv2.face.EigenFaceRecognizer_create()

	createFisherFaceRecognizer(...)

	createLBPHFaceRecognizer(...)
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	

Quick way to check if "Basic Face Recognizer" is empty or not.
	
	python3
	import cv2
	test = help(cv2.face_BasicFaceRecognizer)

How to resolve :

	cv2.error: /Users/travis/build/skvark/opencv-python/opencv_contrib/modules/face/src/eigen_faces.cpp:117: error: (-2) This Eigenfaces model is not computed yet. Did you call Eigenfaces::train? in function predict

	This can happen in the detector.

	Cause:
	The trainner.xml was not created with the EigenFaceRecognizer()
	and you were running the detector which had the EigenFaceRecognizer.

	

	How to resolve :
		build the trainer and the detector with the same face recognizer.
		If EigenFaceRecognizer. Then train with EigenFaceRecognizer.
		If LBPH then train and detector with the same Recognizer.


Types of IMREAD_

* IMREAD_COLOR If the flag is set to this value, the loaded image will be converted to a 3-channel BGR (Blue Green Red) color image.

* IMREAD_GRAYSCALE If the flag is set to this value, the loaded image will be converted to a single-channel grayscale image.

* IMREAD_LOAD_GDAL If the flag is set to this value, you can load the image using the gdal driver.
	
* IMREAD_ANYCOLOR If the flag is set to this value, the image is read in any possible color format.


### Check which version of cv2

	python3
	import cv2
	cv2.__version__
	'3.4.0'


To Create the data set using the WebCam IP app

        **python3 facialrecognitionIPWebcam.py**

To Create the data set using the Laptop WebCam 

	**python3  facialrecognition.py**


To detect both the "eyes" and the "face" using the classifiers:  during the facial detection

http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
