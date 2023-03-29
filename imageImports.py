import pygame
pygame.init()

inventoryImage = pygame.image.load(r"images\inventory.png")

backpack = pygame.image.load(r"images\backpack.png")
backpackRect = backpack.get_rect(topleft = (10,10))

closeButton = pygame.image.load(r"images\close.png")
closeRect = closeButton.get_rect(topleft = (342, 10))

stoneButtonUp = pygame.image.load('images\stoneButton.png')
stoneButtonDown = pygame.image.load('images\stoneButton_Down.png')

woodButtonUp = pygame.image.load('images\woodButton.png')
woodButtonDown = pygame.image.load('images\woodButton_Down.png')
