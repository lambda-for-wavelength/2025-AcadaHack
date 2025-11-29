import pygame
import objects

FREE =pygame.Color(61, 117, 32)
WALL = pygame.Color(115, 73, 22)
SPIKE = pygame.Color(89, 85, 80)
CRATE = pygame.Color(115, 22, 22)
LEVER = pygame.Color(84, 32, 117)
ICE = pygame.Color(22, 97, 115)
WWT = pygame.Color(255, 255, 255)

def gen_map(image: pygame.Surface, groups: dict[str:pygame.sprite.Group]):

    final_map = pygame.Surface((image.get_width() * 32, image.get_height() * 32))

    for x in range (32):
        for y in range(32):
            pixel = image.get_at((x, y))
            if pixel == FREE:
                i = objects.Free(x*32, y*32)
                groups['FREE'].add(i)
            elif pixel == WALL:
                i = objects.Wall(x*32, y*32)
                groups['WALL'].add(i)
            elif pixel == SPIKE:
                pass
            elif pixel == CRATE:
                pass
            elif pixel == LEVER:
                pass
            elif pixel == ICE:
                pass
            elif pixel == WWT:
                pass