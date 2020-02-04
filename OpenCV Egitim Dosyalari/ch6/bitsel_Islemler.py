import cv2
import numpy as np


dikdortgen = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(dikdortgen, (25, 25), (275, 275), 255, -1)
cv2.imshow("dikdortgen", dikdortgen)

daire = np.zeros((300, 300), dtype = "uint8")
cv2.circle(daire, (150, 150), 150, 255, -1)
cv2.imshow("daire", daire)

bitselAnd = cv2.bitwise_and(dikdortgen, daire)
cv2.imshow("AND", bitselAnd)
cv2.waitKey(0)

bitselOr = cv2.bitwise_or(dikdortgen, daire)
cv2.imshow("OR", bitselOr)
cv2.waitKey(0)

bitselXor = cv2.bitwise_xor(dikdortgen, daire)
cv2.imshow("XOR", bitselXor)
cv2.waitKey(0)

bitselNot = cv2.bitwise_not(daire)
cv2.imshow("NOT", bitselNot)
cv2.waitKey(0)