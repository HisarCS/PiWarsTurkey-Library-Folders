from pololu_drv8835_rpi import motors
import math



class MotorKontrol:

    def __init__(self):
        self.hizSag = 0
        self.hizSol = 0

    def hizlariAyarla(self, hizSag, hizSol):

        self.hizSag = hizSag
        self.hizSol = hizSol

        480 if hizSag>480 else hizSag
        -480 if hizSag < -480 else hizSag

        480 if hizSol > 480 else hizSol
        -480 if hizSol < -480 else hizSol



        motors.setSpeeds(hizSag, hizSol)

    def kumandaVerisiniMotorVerilerineCevirme(self, x, y, t):
        if (t):
            if (math.copysign(1, x) != math.copysign(1, y)):
                return (int)((-y + x) * 240)
            else:
                return (int)((-y + x) * 480)
        else:
            if (math.copysign(1, x) == math.copysign(1, y)):
                return (int)((-y - x) * 240)
            else:
                return (int)((-y - x) * 480)
