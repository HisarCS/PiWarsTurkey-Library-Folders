import cv2
import os
import numpy as np

logo = cv2.imread(os.path.abspath('PiWarsTurkeyLogo.png'))
cv2.imshow("Logo Asil", logo)
cv2.waitKey(0)

# öteleme
M = np.float32([[1,0,50], [0,1,25]])
kaydirilmis = cv2.warpAffine(logo, M , (logo.shape[1],logo.shape[0]) )
cv2.imshow("Kaydirilmis Resim",kaydirilmis)
cv2.waitKey(0)

#dondurme
merkez = (logo.shape[1] // 2,logo.shape[0] // 2)
M = cv2.getRotationMatrix2D(merkez, 45, 1.0)
dondurulmus = cv2.warpAffine(logo, M, (logo.shape[1],logo.shape[0]))
cv2.imshow("45 Derece Dondurulmus Resim", dondurulmus)
cv2.waitKey(0)

#yeniden boyutlandirma
yeni_boyutlar = (logo.shape[1] // 2, logo.shape[0] // 2 )
yenidenBoyutlandirilmis = cv2.resize(logo, yeni_boyutlar, interpolation = cv2.INTER_AREA)
cv2.imshow("Yeniden Boyutlandırılmış", yenidenBoyutlandirilmis)
cv2.waitKey(0)

#yansıma
yansima = cv2.flip(logo,1) #  0==> dikey  ,  1==> yatay  ,  -1==> ikisi de
cv2.imshow("yatay eksende yansitilmis",yansima)
cv2.waitKey(0)

#kirpma
logodanBirParca = logo.copy()[0:387, 0:220]
cv2.imshow("LogodanBirParca", logodanBirParca)
cv2.waitKey(0)
