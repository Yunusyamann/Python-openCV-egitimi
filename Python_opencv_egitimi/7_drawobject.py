import cv2 as cv
import numpy as np

# Siyah bir arka plan oluşturun
width, height = 640, 480
black_bg = np.zeros((height, width, 3), dtype=np.uint8)

# Dikdörtgen çizimi
cv.rectangle(black_bg, (50, 50), (200, 150), (0, 255, 0), 2)  # Sol üst köşe ve sağ alt köşe koordinatları, renk ve kalınlık

# Çember çizimi
cv.circle(black_bg, (300, 150), 50, (255, 0, 0), 3)  # Merkez koordinatı, yarıçap, renk ve kalınlık

# Çizgi çizimi
cv.line(black_bg, (400, 50), (550, 150), (0, 0, 255), 5)  # Başlangıç ve bitiş koordinatları, renk ve kalınlık

# Yazı ekleme
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(black_bg, 'OpenCV', (50, 300), font, 1, (255, 255, 255), 2, cv.LINE_AA)  # Metin, konum, yazı tipi, boyut, renk, kalınlık ve stil

# Pencereyi göster
cv.imshow('Geometrik Cisimler', black_bg)
cv.waitKey(0)
cv.destroyAllWindows()
 