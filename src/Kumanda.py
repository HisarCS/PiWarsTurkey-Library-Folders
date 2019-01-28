import pygame
from threading import Thread


class Kumanda:

    def __init__(self):

        pygame.init()

        pygame.joystick.init()

        self.j = pygame.joystick.Joystick(0)
        self.j.init()


        self.buttons = []
        self.lx = 0
        self.ly = 0
        self.i = 0

    def dinlemeyeBasla(self):

        Thread(target=self.guncelle, args=()).start()
        return self

    def guncelle(self):

        while True:

            for e in pygame.event.get():
                if (e.type == pygame.JOYAXISMOTION):
                    if (e.axis == 0):
                        self.lx = e.value
                    elif (e.axis == 1):
                        self.ly = e.value

    def verileriOku(self):

        return self.lx, self.ly

