import numpy as np
import cv2

file="training-data/two.png"
font = cv2.FONT_HERSHEY_SIMPLEX

#image_flag = ["cv2.IMREAD_GRAYSCALE", "cv2.IMREAD_COLOR" ] 
#print ( image_flag )

# Load an color image in grayscale
img = cv2.imread(file,cv2.IMREAD_COLOR)
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,300)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

cv2.putText(img,'Hello World!',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor,
    lineType)

cv2.imshow('image',img)
# any key on the image.
cv2.waitKey(0)

cv2.destroyAllWindows()
