#RESİM OKUMA
import cv2 as cv
# dosya yolunu path değişkenine atadık
path = r"C:\Users\yunus\Downloads\resim.png"
# görüntüyü okuduk
img = cv.imread(path)
# eğer görüntü başarılı bir şekilde yüklenmediyse uyarı verelim
    # pencereyi oluşturduk
#RESMİ GRİYE ÇEVİRME:
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.namedWindow("opencvtest", cv.WINDOW_AUTOSIZE)
    # görüntüyü pencerede gösterdik
cv.imshow("opencvtest", img)
cv.imshow("opencvtest", gray )
    # herhangi bir tuşa basılana kadar bekledik
cv.waitKey(0)
    # tüm pencereleri kapattık
cv.destroyAllWindows()

#resmi bir dizine kaydetme
cv.imwrite(path+ "gray_opencv.png",gray)

#resmi direk  gri olarak okumak için :
# img=cv.imread(path+"resim.png",cv.IMREAD_GRAYSCALE) 