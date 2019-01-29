from time import sleep, time
import RPi.GPIO as GPIO
from threading import Thread
import time

class ServoKontrol:
    
    def __init__(self, pin=35, GPIOSetup = GPIO.BOARD):
        GPIO.setmode(GPIOSetup)
        
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.pin = pin
        self.desiredAngle = 90
        self.currentAngle = 90
        self.setState = False
        self.gotSleep = True
        self.continous = False
        
        print("const. calisti")
    
    def surekliDonmeyeAyarla(self):
        self.continous = True
        GPIO.output(self.pin, True)
    
    def tekDonmeyeAyarla(self):
        self.continous = False
        GPIO.output(self.pin, False)
    
    def __aciAyarlaAsil__(self):
        duty = self.desiredAngle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        deltaAngle = abs(self.desiredAngle - self.currentAngle)
        sleepNeeded = deltaAngle / 270
        
        print(sleepNeeded)
        sleep(deltaAngle / 150)  # experimental value
        self.gotSleep = True
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.currentAngle = self.desiredAngle
    
    def surekliDondurAsil(self, aci):
        duty = aci / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
    
    def aciAyarla(self, aci):
        if self.continous:
            self.surekliDondurAsil(aci)
        elif self.gotSleep and (self.currentAngle is not aci):
            self.gotSleep = False
            self.desiredAngle = aci
            
            Thread(target=self.aciAyarlaAsil, args=()).start()
