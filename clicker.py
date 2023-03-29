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

score= 0
font = pygame.font.Font('freesansbold.ttf', 16)
scoreText = font.render(str(score), True, (0,0,0))
scoreRect = scoreText.get_rect(topleft = (200 - score//10, 50))

#buttons are 80 wide, 30 tall

stoneBar = healthBar(screen, (140, 80), (150,150,150), (200,200,200))
woodBar = healthBar(screen, (140, 140), (145, 82, 4), (171, 99, 10))

stoneProg = 0
stoneButton = stoneButtonUp
stoneButtonRect = stoneButton.get_rect(topleft = (30, 80))
stoneBarIncreasing = False

woodButton = woodButtonUp
woodButtonRect = woodButton.get_rect(topleft = (30, 140))

smallFont = pygame.font.Font('freesansbold.ttf', 12)

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
        
    
    woodButton = woodButtonUp
    stoneButton = stoneButtonUp
    pygame.display.flip()
    clock.tick(framerate)  
