import cv2 as cv

# HSV, renkleri ifade etmek için sıkça kullanılan bir renk modelidir. 
# HSV, Hue (ton), Saturation (doygunluk) ve Value (değer) kelimelerinin baş harflerinden oluşur.

img=cv.imread(r"C:\Users\yunus\Downloads\resim.png")

#normal hali 
cv.namedWindow("rgb",cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(1)

#griye cevrime
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)

#HSV nesnelerinin takibini kolaylaştırır.
#hsv format: 
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(0)



