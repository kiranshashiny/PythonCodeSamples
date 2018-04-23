import cv2

cap = cv2.VideoCapture(0)
address = "http://192.168.1.5:8080/video" # Your address might be different
detector=cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')


Id=input('Enter your id  ')
sampleNum=0


cap.open(address)

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

# Read and display video frames until video is completed or 
# user quits by pressing ESC
sampleNum =1

cv2.startWindowThread()


while(cap.isOpened()):
    # Capture frame-by-frame
    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            # Display the resulting frame
            cv2.imshow('Frame',img)
            sampleNum = sampleNum +1
            print ( "sample # ", sampleNum )
            #saving the captured face in the dataset folder
            cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

    else:
        break

    # finally
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    if sampleNum > 20 :
        break
    
cap.release()
cv2.destroyAllWindows()
