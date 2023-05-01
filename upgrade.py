import pygame

class Upgrade:
    def __init__(self) -> None:
        self.img = pygame.Surface((280, 160))
        self.img.fill((0,0,0))
        self.rect = pygame.rect.Rect(110,40,280,160)