import cv2 as cv
import numpy as np 

path = r"C:\Users\yunus\Downloads\resim.png"
src = cv.imread(path, cv.IMREAD_GRAYSCALE)  # Resmi gri tonlamalı olarak yükle



# Minimum ve maksimum değerleri ile konumlarını hesapla
min_deger, max_deger, min_konum, max_konum = cv.minMaxLoc(src)
print("Minimum değer: %.2f, maksimum değer: %.2f" % (min_deger, max_deger))
print("Minimum konum:", min_konum, ", maksimum konum:", max_konum)

    # Ortalama ve standart sapmayı hesapla
ortalama, standart_sapma = cv.meanStdDev(src)
print("Ortalama: %.2f, standart sapma: %.2f" % (ortalama[0][0], standart_sapma[0][0]))


#resmi sadece siyah ve beyaz yapma:
src[np.where(src<ortalama)] =0
src[np.where(src>ortalama)] =255
cv.imshow("binary",src)
cv.waitKey(0)
