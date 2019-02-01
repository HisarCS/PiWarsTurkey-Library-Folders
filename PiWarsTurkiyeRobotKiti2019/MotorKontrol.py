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

    def differentialDrive(self, x, y):
        if(x == 0 and y == 0):
		return (0, 0)

        z = math.sqrt(x * x + y * y)
        angle = math.acos(math.fabs(x) / z) * 180 / math.pi

        tcoeff = -1 + (angle / 90) * 2
        turn = tcoeff * math.fabs(math.fabs(y) - math.fabs(x))
        turn = round(turn * 100, 0) / 100

        mov = max(math.fabs(y), math.fabs(x))

        if (x >= 0 and y <= 0) or (x < 0 and y > 0):
             rawLeft = mov
             rawRight = turn
        else:
             rawRight = mov
             rawLeft = turn

        if y < 0:
            rawLeft = -rawLeft
            rawRight = -rawRight

        rightOut = map(rawRight, -1, 1, -480, 480)
        leftOut = map(rawLeft, -1, 1, -480, 480)

        return(rightOut, leftOut)

    def map(v, in_min, in_max, out_min, out_max):
        if v < in_min:
             v = in_min
        if v > in_max:
            v = in_max
        return (v - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
