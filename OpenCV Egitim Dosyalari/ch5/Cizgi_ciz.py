import cv2
import numpy as np

tuval = np.zeros((500, 500, 3), dtype = "uint8")
cv2.imshow('siyah', tuval)
cv2.waitKey(0)


yesil = (0, 255, 0)
cv2.line(tuval, (0, 0), (500, 500), yesil)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)

kirmizi = (0, 0, 255)
cv2.line(tuval, (500, 0), (0, 500), kirmizi, 3)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)

cv2.rectangle(tuval, (30, 30), (120, 120), kirmizi, 3)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)

cv2.rectangle(tuval, (200, 200), (300, 300), yesil, -1)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)

beyaz = (255, 255, 255)
cv2.circle(tuval, (tuval.shape[1] // 2, tuval.shape[0] // 2), 30, beyaz)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)

cv2.circle(tuval, (tuval.shape[1] // 2, tuval.shape[0] // 2), 100, yesil, -1)
cv2.imshow('Cizgili Tuval', tuval)
cv2.waitKey(0)