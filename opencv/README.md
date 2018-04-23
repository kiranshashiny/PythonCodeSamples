

	img = cv2.imread('trump.png')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if ( len( gray) ==0 ):
		print ("image is empty")
	else :
		print ("Image is good")

The FaceRecognizers are :

	createEigenFaceRecognizer(...)
	recognizer = cv2.face.EigenFaceRecognizer_create()

	createFisherFaceRecognizer(...)

	createLBPHFaceRecognizer(...)
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainner.yml')



quick way to check if Basic Face recognizer is there or not.
	
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

