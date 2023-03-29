import pygame

def onClick(objectRect):
    mx, my = pygame.mouse.get_pos()

    if objectRect.topleft[0] < mx:
        if objectRect.topleft[1] < my:
            if objectRect.bottomright[0] > mx:
                if objectRect.bottomright[1] > my:
                    return True
    return False