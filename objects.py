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
        self.groups_list = []
        self.dir = pygame.Vector2(0,0)

    def update(self, dt, *args, **kwargs):
        self.timer += dt
        #this is just moving around
        if self.timer >= TICK_RATE:
            self.dir = pygame.Vector2(0,0)
            Key = pygame.key.get_pressed()
            if Key[pygame.K_w] == True:
                self.rect.move_ip(0, -32)
                self.dir.y = -1
            elif Key[pygame.K_a] == True:
                self.rect.move_ip(-32, 0)
                self.dir.x = -1
            elif Key[pygame.K_s] == True:
                self.rect.move_ip(0, +32)
                self.dir.y = 1
            elif Key[pygame.K_d] == True:
                self.rect.move_ip(+32, 0)
                self.dir.x = 1
            self.timer = 0
        #pushing crates
        Crates = pygame.sprite.spritecollide(self, self.groups_list[0], False)
        if len(Crates):
            for c in Crates:
                c.rect.move_ip(32 * self.dir.x, 32 * self.dir.y)


class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Crate.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Wall.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class FREE(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Free.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class SPIKE(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Spike.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class LEVER(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Lever.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ICE(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Ice.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class WWT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/WWT.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)