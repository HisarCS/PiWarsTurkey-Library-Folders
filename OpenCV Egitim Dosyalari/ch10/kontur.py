import cv2
import os

paralar = cv2.imread(os.path.abspath('paralar.jpeg'))
cv2.imshow('Paralar',paralar)

gri = cv2.cvtColor(paralar, cv2.COLOR_BGR2GRAY)
bulanik = cv2.GaussianBlur(gri, (11, 11), 0)
cv2.imshow("Bulanik", bulanik)

esik = cv2.adaptiveThreshold(bulanik, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Esik", esik)


(kntr, _ ) = cv2.findContours(esik.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Gorselde {} tane bozuk para buldum".format(len(kntr)))

paralarKontur = paralar.copy()
cv2.drawContours(paralarKontur, kntr, -1, (0,255,0), 2)
cv2.imshow("Paralar Konturlu", paralarKontur)
cv2.waitKey(0)
