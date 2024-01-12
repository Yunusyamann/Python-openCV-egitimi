import cv2 as cv

path = r"C:\Users\yunus\Downloads\resim.png"

# Görüntüyü okuduk
img = cv.imread(path)

# Görüntüyü başarıyla okuduysak işlemlere devam ediyoruz
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
h, w, ch = img.shape
print("h,w,ch:", h, w, ch)

  # Beyaz pikselleri siyah yapma
for i in range(h):
        for j in range(w):
            # Eğer pikselin tüm kanalları 255 ise (beyaz), pikseli siyah yap (0, 0, 0)
            if all(img[i, j] == 255):
                img[i, j] = [0, 0, 0]  # Siyah

    # Görüntüyü göster
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
 