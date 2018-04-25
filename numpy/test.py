
loop:
while ( ) 
	read input from video () ) 
	
	get the image
	convert image to gray_img
	
	faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  
	
	#print the number of faces found 
	print('Faces found: ', len(faces))
	
	if ( ret == 0 ) ;
		go back to loop.
	
	
	if (ret == 1):
		print ("got 1 face")
	elif ( ret ==2 ): 
		print ("got 2 face ")
	
	else :
		print ("Got >2 ")
	
		do something
		turn light on
		close gate
		or send a sms to Whtie house security
	
	
	sleep (0.5 ) 

	
