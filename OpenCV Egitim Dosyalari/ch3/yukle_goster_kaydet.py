import cv2
import os

logonunAdresi = os.path.abspath('PiWarsTurkeyLogo.png')

print(logonunAdresi)

logo = cv2.imread(logonunAdresi)

cv2.imshow("Logo Resmi", logo)
cv2.waitKey(0)

print("uzunluk: {} piksel".format(logo.shape[0]))
print("genişlik: {} piksel".format(logo.shape[1]))
print("kanal sayısı: {} ".format(logo.shape[2]))



cv2.imwrite("LogoKopyası.jpeg", logo)

