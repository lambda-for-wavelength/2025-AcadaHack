import pygame

FREE =pygame.color(61, 117, 32)
WALL = pygame.color(115, 73, 22)
SPIKE = pygame.color(89, 85, 80)
CRATE = pygame.color(115, 22, 22)
SWITCH = pygame.color(84, 32, 117)
ICE = pygame.color(22, 97, 115)
WWT = pygame.color(255, 255, 255)

def gen_map(image: pygame.Surface):

    final_map = pygame.Surface((image.width* 32, image.height * 32))

    for x in range (32):
        for y in range(32):
            pixel = image.get_at((x, y))
            if pixel == FREE:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == WALL:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == SPIKE:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == CRATE:
                #final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == SWITCH:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == ICE:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))
            elif pixel == WWT:
                final_map.blit("text hear", pygame.Rect(x*32, y*32, 32, 32))