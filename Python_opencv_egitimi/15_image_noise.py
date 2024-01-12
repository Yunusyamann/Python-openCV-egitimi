import cv2 as cv
import numpy as np

def add_salt(image):
    h, w = image.shape[:2]
    nums = 10000  # Rastgele nokta sayısı
    rows = np.random.randint(0, h, nums, dtype=int)
    cols = np.random.randint(0, w, nums, dtype=int)
    
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)  # Beyaz nokta ekleme
        else:
            image[rows[i], cols[i]] = (0, 0, 0)  # Siyah nokta ekleme
    return image

# Resmi yükle
path = r"C:\Users\yunus\Downloads\resim.png"  # Resminizin dosya yolunu buraya girin
src = cv.imread(path)

if src is None:
    print("Resim yüklenemedi. Dosya yolunu kontrol edin.")
else:
    copy = np.copy(src)
    copy = add_salt(copy)

    # Oluşan görüntüleri yan yana göstermek için bir pencere oluştur
    result = np.hstack((src, copy))

    cv.imshow("Orijinal ve Gürültülü Görüntü", result)
    cv.waitKey(0)

cv.destroyAllWindows()
