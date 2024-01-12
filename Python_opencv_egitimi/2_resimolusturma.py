import cv2 as cv
import numpy as np 

path = r"C:\Users\yunus\Downloads\resim.png"
img = cv.imread(path)  # Corrected the image path here
cv.namedWindow("image_create", cv.WINDOW_AUTOSIZE)
cv.imshow("img_create", img)
cv.waitKey(1)  # Changed the waitKey parameter to 0 to wait indefinitely until a key is pressed

m1 = np.copy(img) 
m2 = img

img[100:200, 200:300, :] = 0

cv.imshow("m2",m2)
cv.waitKey(0)

m3=np.zeros(img.shape,np.uint8)
cv.imshow("m3",m3)
cv.waitKey(0)

m4=np.zeros(img.shape,img.dtype)
cv.imshow("m4",m4)
cv.waitKey(0)
 