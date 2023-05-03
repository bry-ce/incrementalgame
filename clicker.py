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
gold = 0

largeFont = pygame.font.Font(pygame.font.get_default_font(), 32)
font = pygame.font.Font(pygame.font.get_default_font(), 20)
smallfont = pygame.font.Font(pygame.font.get_default_font(), 12)
goldAmt = font.render(str(gold)+ " Coins", True, (0,0,0))
goldAmtRectMain = pygame.rect.Rect(260, 15, 100, 20)
goldAmtRectSecondary = pygame.rect.Rect(75, 60, 100, 20)

current_time = pygame.time.get_ticks()
axelvl = 1
picklvl = 1
pickUpgradeStonePrice = (3*picklvl)
pickUpgradeWoodPrice = (2*picklvl)

reforgeFont = pygame.font.Font(pygame.font.get_default_font(), 20)
reforgeText = reforgeFont.render("Reforge -  10 Gold", True, (0,0,0))
reforgeTextRect = pygame.rect.Rect(87, 616, 300, 200)
bonusText = smallfont.render("Current Reforge Bonus: ", True, (0,0,0))

pickUpgradeText = font.render("Upgrade Pickaxe", True, (0,0,0))
pickUpgradeTextRect = pygame.rect.Rect(90, 130, 100, 100)

pickUpgradePriceText = smallfont.render(str(pickUpgradeStonePrice) + " Stone, " + str(pickUpgradeWoodPrice) + " wood", True, (0,0,0))
pickUpgradePriceRect = pygame.rect.Rect(90, 155, 100, 100)
stoneAmt = font.render(str(stone)+ " Stone", True, (0,0,0))
stoneAmtRect = pygame.rect.Rect(75, 220, 40, 40)

woodAmt = font.render(str(wood) + " Wood", True, (0,0,0))
woodAmtRect = pygame.rect.Rect(75, 270, 40, 40)
#buttons are 80 wide, 30 tall

stoneBar = healthBar(screen, (140, 80), (150,150,150), (200,200,200), stone, 1, picklvl)
woodBar = healthBar(screen, (140, 140), (145, 82, 4), (171, 99, 10), wood, 1.3, axelvl)

stoneButton = stoneButtonUp
stoneButtonRect = stoneButton.get_rect(topleft = (30, 80))
stoneBarIncreasing = False

woodButton = woodButtonUp
woodButtonRect = woodButton.get_rect(topleft = (30, 140))

inventory = False
upgradeMenu = False
lastMineAnimationUpdate =  current_time
mineframe = 0
mineAnimRect = mineAnimList[mineframe].get_rect(topleft = (300, 80))

lastWoodAnimationUpdate =current_time
woodframe = 0
woodAnimRect = woodAnimList[woodframe].get_rect(topleft = (300, 130))
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
                elif onClick(pickaxeUpgradeRect):
                    pickUpButton = pickaxeUpgradeDown
                    if (stone >= int(pickUpgradeStonePrice) and wood >= pickUpgradeWoodPrice):
                        stoneBar.resource -= int(pickUpgradeStonePrice)
                        woodBar.resource -= int(pickUpgradeWoodPrice)
                        picklvl += 1
                        pickUpgradeStonePrice = (3*picklvl)
                        pickUpgradeWoodPrice = (2*picklvl)
                        pickUpgradePriceText = smallfont.render(str(pickUpgradeStonePrice) + " Stone, " + str(pickUpgradeWoodPrice) + " wood", True, (0,0,0))
                elif onClick(regforgeButtonRect):
                    reforgeButton = reforgeDown

    stone = stoneBar.resource
    wood = woodBar.resource

    if inventory:
        screen.blit(inventoryImage, (0,0))
        screen.blit(closeButton, closeRect)
        screen.blit(stoneAmt, stoneAmtRect)
        screen.blit(rockImg, rockRect)
        screen.blit(logImg, logRect)
        screen.blit(woodAmt, woodAmtRect)
    elif upgradeMenu:
        screen.blit(backpack, backpackRect)
        screen.blit(closeButton, closeRect) 
        pygame.draw.rect(screen, (170,170,170), pygame.rect.Rect(50, 100, 300, 500))
        screen.blit(pickUpButton, pickaxeUpgradeRect)
        screen.blit(pickUpgradeText, pickUpgradeTextRect)
        screen.blit(pickUpgradePriceText, pickUpgradePriceRect)
    else:
        screen.blit(cavebg, cavebgRect); screen.blit(stoneButton, stoneButtonRect)
        screen.blit(woodbg, woodbgRect); screen.blit(woodButton, woodButtonRect)
        screen.blit(backpack, backpackRect)
        screen.blit(upgradeButton, upgradeRect)
        screen.blit(reforgeButton, regforgeButtonRect); screen.blit(reforgeText, reforgeTextRect)
        screen.blit(bonusText, (10, 550))
        stoneBar.update()
        woodBar.update()
        

    if stoneBar.increasing and inventory == False and upgradeMenu == False:
        if current_time-lastMineAnimationUpdate > 300:
            mineframe += 1
            lastMineAnimationUpdate = current_time
            if mineframe > 1:
                mineframe = 0
        screen.blit(mineAnimList[mineframe], mineAnimRect)
    
    if woodBar.increasing and inventory == False and upgradeMenu == False:
        if current_time -lastWoodAnimationUpdate > 300:
            woodframe += 1
            lastWoodAnimationUpdate = current_time
            if woodframe > 1:
                woodframe = 0
        screen.blit(woodAnimList[woodframe], woodAnimRect)
    #print(current_time, lastMineAnimationUpdate)


    stoneBar.lvl = picklvl 
    woodButton = woodButtonUp
    stoneButton = stoneButtonUp
    pickUpButton = pickaxeUpgradeUp
    reforgeButton = reforgeUp
    print("stone:", stone, "price: ", pickUpgradeStonePrice, " Level:  " , picklvl)
    pygame.display.flip()
    clock.tick(framerate)  
