import pygame

TICK_RATE = 80

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill("white")
        self.rect.topleft = (x, y)
        self.timer = 0

    def update(self, dt, *args, **kwargs):
        self.timer += dt
        if self.timer >= TICK_RATE:
            Key = pygame.key.get_pressed()
            if Key[pygame.K_w] == True:
                self.rect.move_ip(0, -32)
            elif Key[pygame.K_a] == True:
                self.rect.move_ip(-32, 0)
            elif Key[pygame.K_s] == True:
                self.rect.move_ip(0, +32)
            elif Key[pygame.K_d] == True:
                self.rect.move_ip(+32, 0)
            self.timer = 0

class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Crate.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)