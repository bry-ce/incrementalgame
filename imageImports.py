import pygame
pygame.init()

inventoryImage = pygame.image.load(r"images\inventory.png")

goldCoin = pygame.image.load(r"images\goldCoin.png")
goldCoinRectMain = goldCoin.get_rect(topleft = (215,5))
goldCoinRectSecondary = goldCoin.get_rect(topleft = (25,50))

backpack = pygame.image.load(r"images\backpack.png")
backpackRect = backpack.get_rect(topleft = (10,10))

closeButton = pygame.image.load(r"images\close.png")
closeRect = closeButton.get_rect(topleft = (342, 10))

stoneButtonUp = pygame.image.load('images\stoneButton.png')
stoneButtonDown = pygame.image.load('images\stoneButton_Down.png')

woodButtonUp = pygame.image.load('images\woodButton.png')
woodButtonDown = pygame.image.load('images\woodButton_Down.png')

rockImg = pygame.image.load(r'images\rock.png')
rockRect = rockImg.get_rect(topleft = (10,210))

logImg = pygame.image.load(r"images\log.png")
logRect = logImg.get_rect(topleft = (7, 245))

upgradeButton = pygame.image.load(r"images\upgrade.png")
upgradeRect = upgradeButton.get_rect(topleft = (65, 12))

mineAnim1 = pygame.image.load(r"images\mineFrameOne.png")
mineAnim2 = pygame.image.load(r"images\mineFrameTwo.png")
mineAnimList = [mineAnim1, mineAnim2]
