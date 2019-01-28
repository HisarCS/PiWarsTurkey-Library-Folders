
from time import sleep
import RPi.GPIO as GPIO
from threading import Thread

class ServoKontrol:

    def __init__(self, pin, setup=GPIO.BOARD):

        GPIO.setmode(setup)
        self.pin = pin

        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)

        self.pwm.start(0)
        self.istenilenAci = 90
        self.suankiAci = 90
        self.uyuduMu = True


    def guncelle(self):

        dutyCycle = self.istenilenAci / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(dutyCycle)
        deltaAci = abs(self.istenilenAci - self.suankiAci)
        gerekenUyku = deltaAci/270
        self.uyuduMu = False
        print(gerekenUyku)
        sleep(deltaAci / 270)  # experimental value
        self.uyuduMu = True


        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.suankiAci = self.istenilenAci


    def aciAyarla(self, aci):

        if self.uyuduMu:
            self.istenilenAci = aci
            Thread(target=self.guncelle, args=()).start()

