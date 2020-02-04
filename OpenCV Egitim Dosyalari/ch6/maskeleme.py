import cv2
import os
import numpy as np


logo = cv2.imread(os.path.abspath('PiWarsTurkeyLogo.png'))
cv2.imshow("Logo Asil", logo)


dikdortgen = np.zeros((logo.shape[0], logo.shape[1]), dtype = "uint8")
cv2.rectangle(dikdortgen, (0, 0), (220, 387), 255, -1)
cv2.imshow("dikdortgen", dikdortgen)


bitselAnd = cv2.bitwise_and(logo, logo, mask = dikdortgen)
cv2.imshow("Maskeli", bitselAnd)
cv2.waitKey(0)


