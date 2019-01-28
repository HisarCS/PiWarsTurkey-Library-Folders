
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread

import cv2

class HizlandirilmisPiKamera:

    def __init__(self, cozunurluk=(640, 480)):

        self.camera = PiCamera()
        self.camera.resolution = cozunurluk
        self.hamKare = PiRGBArray(self.camera, size=self.camera.resolution)
        self.yayin = self.camera.capture_continuous(self.hamKare, format="bgr", use_video_port=True)

        self.suAnkiKare = None

    def veriOkumayaBasla(self):

        Thread(target=self.verileriGuncelle, args=()).start()
        return self

    def veriGuncelle(self):

        for f in self.yayin:

            self.suAnkiKare = f.array
            self.hamKare.truncate(0)

    def veriOku(self):

        return self.suAnkiKare

    def kareyiGoster(self):
        Thread(target=self.kareyiGostermeyiGuncelle, args=()).start()

    def kareyiGostermeyiGuncelle(self):

        while True:
            cv2.imshow("frame", self.suAnkiKare)

            key = cv2.waitKey(1)

            if key == ord("q"):
                cv2.destroyAllWindows()
                break
