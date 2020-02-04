import cv2
import os
import numpy as np


logo = cv2.imread(os.path.abspath('PiWarsTurkeyLogo.png'))
cv2.imshow("Logo Asil", logo)
cv2.waitKey(0)

M = np.ones(logo.shape, dtype = "uint8") * 100

added = cv2.add(logo, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

subtracted = cv2.subtract(logo, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
