

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



quick way to test it :
	
	python3
	import cv2
	test = help(cv2.face_BasicFaceRecognizer)




	
