import pygame
from sys import exit
from onClick import *
from healthbar import *
from imageImports import *
framerate = 24

pygame.init()
screen = pygame.display.set_mode((400,700))
clock = pygame.time.Clock()

bars = []
stone = 0
wood = 0



font = pygame.font.Font(pygame.font.get_default_font(), 20)
stoneAmt = font.render(str(stone)+ " Stone", True, (0,0,0))
stoneAmtRect = pygame.rect.Rect(75, 220, 40, 40)

woodAmt = font.render(str(wood) + " Wood", True, (0,0,0))
woodAmtRect = pygame.rect.Rect(75, 270, 40, 40)
#buttons are 80 wide, 30 tall

stoneBar = healthBar(screen, (140, 80), (150,150,150), (200,200,200), stone)
woodBar = healthBar(screen, (140, 140), (145, 82, 4), (171, 99, 10), wood)

stoneProg = 0
stoneButton = stoneButtonUp
stoneButtonRect = stoneButton.get_rect(topleft = (30, 80))
stoneBarIncreasing = False

woodButton = woodButtonUp
woodButtonRect = woodButton.get_rect(topleft = (30, 140))

inventory = False

while True:
    screen.fill('#9EA9FF')
    mouseposx, mouseposy = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if onClick(stoneButtonRect):
                    stoneBar.increasing = True
                    stoneButton = stoneButtonDown
                if onClick(woodButtonRect):
                    woodBar.increasing = True
                    woodButton = woodButtonDown
                if onClick(backpackRect):
                    inventory = True
                    stone = stoneBar.resource
                    stoneAmt = stoneAmt = font.render(str(stone) + " Stone", True, (0,0,0))

                    wood = woodBar.resource
                    woodAmt = font.render(str(wood) + " Wood", True, (0,0,0))

                if onClick(closeRect):
                    inventory = False

    if not inventory:
        screen.blit(woodButton, woodButtonRect)
        screen.blit(stoneButton, stoneButtonRect)
        screen.blit(backpack, backpackRect)
        stoneBar.update()
        woodBar.update()
    else:
        screen.blit(inventoryImage, (0,0))
        screen.blit(closeButton, closeRect)
        screen.blit(stoneAmt, stoneAmtRect)
        screen.blit(rockImg, rockRect)
        screen.blit(logImg, logRect)
        screen.blit(woodAmt, woodAmtRect)
    woodButton = woodButtonUp
    stoneButton = stoneButtonUp
    pygame.display.flip()
    clock.tick(framerate)  
