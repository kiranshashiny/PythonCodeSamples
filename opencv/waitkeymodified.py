#
#
#
# waitkey (0) means wait forever ,or get the input key 'q' and quit.
#
#
#

import cv2

file="training-data/one.png"

img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
# Any 'q' key on the image to get out of the while forever loop.
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
