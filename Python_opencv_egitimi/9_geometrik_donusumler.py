import cv2 as cv
import numpy as np

# Resmi yükle
path = r"C:\Users\yunus\Downloads\resim.png"
image = cv.imread(path)

if image is None:
    print("-")

else:
    # Resmi kaydırma (translation)
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # x=50, y=30 kaydırma
    translated_image = cv.warpAffine(image, translation_matrix, (cols, rows))

    cv.imshow('Kaydırılmış Resim', translated_image)
    cv.waitKey(0)

    # Resmi döndürme (rotation)
    rotation_matrix = cv.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # Merkezi (cols/2, rows/2) noktasında 45 derece döndürme
    rotated_image = cv.warpAffine(image, rotation_matrix, (cols, rows))

    cv.imshow('Döndürülmüş Resim', rotated_image)
    cv.waitKey(0)

    # Resmi yeniden boyutlandırma (resizing)
    resized_image = cv.resize(image, None, fx=0.5, fy=0.5)  # 0.5 oranında boyutlandırma

    cv.imshow('Yeniden Boyutlandırılmış Resim', resized_image)
    cv.waitKey(0)

    # Küçük resim oluşturma
    small_image = image[100:300, 200:400]  # Belirli bir bölgeyi seçme (örneğin: 100-300 satırları, 200-400 sütunları arasındaki bölgeyi seçme)

    cv.imshow('Küçük Resim', small_image)
    cv.waitKey(0)

cv.destroyAllWindows()
