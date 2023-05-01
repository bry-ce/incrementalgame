import pygame, sys, math, random

class healthBar():
    def __init__(self, screen, pos, bgcolor, barcolor, resource, speed, lvl) -> None:
        self.progress = 0
        self.increasing = False
        self.maxWidth = 100
        self.height = 30
        self.bgcolor = bgcolor
        self.barcolor = barcolor
        self.pos = pos
        self.screen = screen
        self.resource = resource
        self.speed = speed
        self.lvl = lvl
        self.image = pygame.Surface((100, 30))
        self.image.fill((50,0,0))

        self.bg = pygame.draw.rect(screen, (bgcolor), pygame.Rect(pos[0],pos[1],self.maxWidth,self.height))
        
        self.bar = pygame.draw.rect(screen, (barcolor), pygame.Rect(pos[0],pos[1],self.maxWidth*self.progress,self.height))

        self.border = pygame.draw.rect(screen, (30,30,30), pygame.Rect(pos[0],pos[1],self.maxWidth,self.height), 1)

    def cycle(self):
        if self.increasing:
            if self.progress < 1:
                self.progress+= (.01 * self.speed)
            else:
                self.progress = 0
                self.increasing = False
                self.resource += (1*self.lvl)

    def update(self):
        self.cycle()
        self.bg = pygame.draw.rect(self.screen, (self.bgcolor), pygame.Rect(self.pos[0],self.pos[1],self.maxWidth,self.height))
        
        self.bar = pygame.draw.rect(self.screen, (self.barcolor), pygame.Rect(self.pos[0],self.pos[1],self.maxWidth*self.progress,self.height))

        self.border = pygame.draw.rect(self.screen, (30,30,30), pygame.Rect(self.pos[0],self.pos[1],self.maxWidth,self.height), 1)

    