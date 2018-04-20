import cv2

fcascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')
fcascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')

if ( fcascade.empty() ):
	print ("Yes empty")
else:
	print ("not empty")

#test2 = cv2.imread('data/test2.jpg')



