

	img = cv2.imread('trump.png')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if ( len( gray) ==0 ):
		print ("image is empty")
	else :
		print ("Image is good")
