import cv2
import os

logo = cv2.imread(os.path.abspath('PiWarsTurkeyLogo.png'))
cv2.imshow("Logo Asil", logo)

birPikselDegeri = logo[300, 500]
print(birPikselDegeri)

logo[300, 500] = (255, 0, 0)
print(logo[300, 500])

logodanBirParca = logo.copy([0:387, 0:220]
cv2.imshow("LogodanBirParca", logodanBirParca)

logo[0:387, 0:220] = (0, 0, 255)
cv2.imshow("Logo Editli", logo)


cv2.waitKey(0)
cv2.imwrite("LogodanBirParca.jpeg", logodanBirParca)

