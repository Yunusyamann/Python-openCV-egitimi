import cv2 as cv

path = r"C:\Users\yunus\Downloads\resim.png"

src=cv.imread(path)

# x flip:
dst1=cv.flip(src,0)
cv.imshow("x-flip",dst1)
cv.waitKey(1)

# y flip:
dst2=cv.flip(src,1)
cv.imshow("y-flip",dst2)
cv.waitKey(0)

# x and y flip:
dst3=cv.flip(src,-1)
cv.imshow("xy-flip", dst3)
cv.waitKey(0)
