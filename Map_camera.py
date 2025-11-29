import pygame
import objects

#this sets the blocks colers for the color map
FREE = pygame.Color(61, 117, 32)
WALL = pygame.Color(115, 73, 22)
SPIKE = pygame.Color(89, 85, 80)
CRATE = pygame.Color(115, 22, 22)
LEVER = pygame.Color(84, 32, 117)
ICE = pygame.Color(22, 97, 115)
WWT = pygame.Color(255, 255, 255)

#this generats all the blocks
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
                i = objects.Spike(x*32, y*32)
                groups['SPIKE'].add(i)
            elif pixel == CRATE:
                i = objects.Free(x*32, y*32)
                groups['FREE'].add(i)
                i = objects.Crate(x*32, y*32)
                groups['CRATE'].add(i)
            elif pixel == LEVER:
                i = objects.Lever(x*32, y*32)
                groups['LEVER'].add(i)
            elif pixel == ICE:
                i = objects.Ice(x*32, y*32)
                groups['ICE'].add(i)
            elif pixel == WWT:
                i = objects.WWT(x*32, y*32)
                groups['WWT'].add(i)