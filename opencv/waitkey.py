#
#
#
# waitkey (25) means wait for 25 milliseconds and then close it
# waitkey (0) means wait forever.
#
#
#

import numpy as np
import cv2

file="training-data/one.png"

image_flag = ["cv2.IMREAD_GRAYSCALE", "cv2.IMREAD_COLOR" ] 
print ( image_flag )

# Load an color image in grayscale
img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
# any key on the image.
cv2.waitKey(3000)  # 3 seconds 
cv2.destroyAllWindows()

img = cv2.imread(file,cv2.IMREAD_COLOR)

cv2.imshow('image',img)
# any key on the image.
cv2.waitKey(25)
cv2.destroyAllWindows()
