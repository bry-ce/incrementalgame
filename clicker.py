import pygame
from sys import exit
from onClick import *
from healthbar import *
from imageImports import *
from animation import *
framerate = 24

pygame.init()
screen = pygame.display.set_mode((400,700))
clock = pygame.time.Clock()

bars = []
stone = 0
wood = 0
gold = 0


font = pygame.font.Font(pygame.font.get_default_font(), 20)
goldAmt = font.render(str(gold)+ " Coins", True, (0,0,0))
goldAmtRectMain = pygame.rect.Rect(260, 15, 100, 20)
goldAmtRectSecondary = pygame.rect.Rect(75, 60, 100, 20)

current_time = pygame.time.get_ticks()


stoneAmt = font.render(str(stone)+ " Stone", True, (0,0,0))
stoneAmtRect = pygame.rect.Rect(75, 220, 40, 40)

woodAmt = font.render(str(wood) + " Wood", True, (0,0,0))
woodAmtRect = pygame.rect.Rect(75, 270, 40, 40)
#buttons are 80 wide, 30 tall

stoneBar = healthBar(screen, (140, 80), (150,150,150), (200,200,200), stone)
woodBar = healthBar(screen, (140, 140), (145, 82, 4), (171, 99, 10), wood)

stoneButton = stoneButtonUp
stoneButtonRect = stoneButton.get_rect(topleft = (30, 80))
stoneBarIncreasing = False

woodButton = woodButtonUp
woodButtonRect = woodButton.get_rect(topleft = (30, 140))

inventory = False
upgradeMenu = False
lastMineAnimationUpdate =  current_time
mineframe = 0
mineAnimRect = mineAnimList[mineframe].get_rect(topleft = (260, 70))


inventoryItemList = [closeButton, stoneAmt, rockImg, logImg, woodAmt, goldAmt, goldCoin]
inventoryItemRectList = [closeRect, stoneAmtRect, rockRect, logRect, woodAmtRect, goldAmtRectSecondary, goldCoinRectSecondary]

upgradeMenuItemList = [backpack, goldCoin, goldAmt, closeButton]
upgradeMenuRectList = [backpackRect, goldCoinRectSecondary, goldAmtRectSecondary, closeRect]

mainScreenItemList = [woodButton, stoneButton, backpack, goldAmt, goldCoin, upgradeButton]
mainScreenRectList = [woodButtonRect, stoneButtonRect, backpackRect, goldAmtRectMain, goldCoinRectMain, upgradeRect]

barUpdateList = [stoneBar, woodBar]


while True:
    screen.fill('#9EA9FF')
    current_time = pygame.time.get_ticks()

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
                elif onClick(woodButtonRect):
                    woodBar.increasing = True
                    woodButton = woodButtonDown
                elif onClick(backpackRect):
                    inventory = True
                    stone = stoneBar.resource
                    stoneAmt = stoneAmt = font.render(str(stone) + " Stone", True, (0,0,0))

                    wood = woodBar.resource
                    woodAmt = font.render(str(wood) + " Wood", True, (0,0,0))
                elif onClick(closeRect):
                    inventory = False
                    upgradeMenu = False
                elif onClick(upgradeRect):
                    upgradeMenu = True


    animationCycle(screen, stoneBar, 300, lastMineAnimationUpdate, 1, mineAnimList, mineAnimRect, inventory, backpack)
    
    # if stoneBar.increasing and inventory == False and upgradeMenu == False:
    #     if current_time-lastMineAnimationUpdate > 300:
    #         mineframe += 1
    #         lastMineAnimationUpdate = current_time
    #         if mineframe > 1:
    #             mineframe = 0
    #     screen.blit(mineAnimList[mineframe], mineAnimRect)

    if inventory:
        screen.blit(inventoryImage, (0,0))
        for item in inventoryItemList:
            for rect in inventoryItemRectList:
                screen.blit(item, rect)
    elif upgradeMenu:
        for item in upgradeMenuItemList:
            for rect in upgradeMenuRectList:
                screen.blit(item, rect)
        pygame.draw.rect(screen, (170,170,170), pygame.rect.Rect(50, 100, 300, 500))
    else:
        for item in mainScreenItemList:
            for rect in mainScreenRectList:
                screen.blit(item, rect)
        for bar in barUpdateList:
            bar.update()
        
    
    #print(current_time, lastMineAnimationUpdate)

    woodButton = woodButtonUp
    stoneButton = stoneButtonUp
    pygame.display.flip()
    clock.tick(framerate)  
