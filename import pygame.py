import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
player = pygame.image.load()
playerrect = player.rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        screen.blit(player, playerrect)

        screen.fill("#95a370")
        pygame.display.update()
        clock.tick(60)