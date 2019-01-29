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
        self.rx = 0
        self.ry = 0
        self.i = 0
    
    def dinlemeyeBasla(self):
        
        Thread(target=self.yenile, args=()).start()
        return self
    
    def yenile(self):
        
        while True:
            for e in pygame.event.get():
                if (e.type == pygame.JOYBUTTONDOWN and e.button not in self.buttons):
                    self.buttons.append(e.button)
                if (e.type == pygame.JOYBUTTONUP and e.button in self.buttons):
                    self.buttons.remove(e.button)
                if (e.type == pygame.JOYAXISMOTION):
                    if (e.axis == 0):
                        self.lx = e.value
                    elif (e.axis == 1):
                        self.ly = e.value
                    elif (e.axis == 2):
                        self.rx = e.value
                    elif (e.axis == 3):
                        self.ry = e.value

    def solVerileriOku(self):
        return self.lx, self.ly
    
    def sagVerileriOku(self):
        return self.rx, self.ry
    
    def butonlariOku(self):
        return self.buttons
    
    def verileriOku(self):
        return self.solVerileriOku(), self.sagVerileriOku(), self.butonlariOku()

