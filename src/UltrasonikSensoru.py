from time import sleep, time
import RPi.GPIO as GPIO



class UltrasonikSensoru:

  def __init__(self, echo, trig, setup=GPIO.BOARD):

    self.echo = echo
    self.trig = trig

    GPIO.setmode(setup)

    GPIO.setup(self.trig,GPIO.OUT)
    GPIO.setup(self.echo,GPIO.IN)

    GPIO.output(trig, False)


  def mesafeOlc(self):

    GPIO.output(self.trig, True)
    sleep(0.0000001)

    sinyal_baslangic = time()

    while GPIO.input(self.echo):
        sleep(0.0000001)
        sinyal_bitis = time()

        sure = sinyal_bitis - sinyal_baslangic

    return sure * 17150
