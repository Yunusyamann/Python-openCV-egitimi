import cv2 as cv

src = cv.imread(r"C:\Users\yunus\Downloads\resim.png")


h, w = src.shape[:2]
print("Genişlik:", w)
print("Yükseklik:", h)
img = src.copy()

# Belirli bir bölgeyi seçme (örnekte 100-350 arası satırlar, 95-530 arası sütunlar)
roi = img[100:350, 95:530, :]

cv.imshow("roi", roi)
cv.waitKey(0)  # Pencerenin kapanmaması için 0 verildi

cv.destroyAllWindows()
