import cv2 as cv
import numpy as np

src = cv.imread(r"C:\Users\yunus\Downloads\resim.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY |cv.THRESH_OTSU)
cv.imshow("thres",gray)
cv.waitKey(0)

#bu yöntem sadece siyah ve beyaz çıktı vererek daha iyi kenar belirler.
