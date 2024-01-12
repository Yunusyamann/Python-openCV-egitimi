import cv2 as cv
import numpy as np

src=cv.imread(r"C:\Users\yunus\Downloads\frame.png")
gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY) # gri skalaya çeviriyoruz.
qrcoder=cv.QRCodeDetector()

codeinfo,points,straight_qrcode=qrcoder.detectAndDecode(gray)

result=np.copy(src)
cv.drawContours(result, [np.int32(points)], -1, (0, 0, 255), 2)


# QR kodunun içindeki metni alıyoruz.
print("Metin: \n%s" % codeinfo)

# Sonucu görselleştirme
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()