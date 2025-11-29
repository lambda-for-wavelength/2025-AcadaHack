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
                wall_above = False
                
                # After this runs, wall_above is True if there is a wall, and False if there is no wall
                for wall in self.groups_list['WALL']: 
                    walls_position = wall.rect.topleft
                    if  walls_position == (self.rect.topleft[0] + 0, self.rect.topleft[1] - 32): #If you try to walk through the block the input doesn't do anything
                        wall_above = True
                # wall_above = True

                if wall_above == False: # If there is no wall above us, we move
                    self.rect.move_ip(0, -32)
                    self.dir.y = -1
            elif Key[pygame.K_a] == True:
                wall_above = False
                
                # After this runs, wall_above is True if there is a wall, and False if there is no wall
                for wall in self.groups_list['WALL']: #warning,list will break,switch to dict
                    walls_position = wall.rect.topleft
                    if  walls_position == (self.rect.topleft[0] - 32, self.rect.topleft[1] + 0): #If you try to walk through the block the input doesn't do anything
                        wall_above = True
                        wall_above = True
                # wall_above = True

                if wall_above == False: # If there is no wall above us, we move
                    self.rect.move_ip(-32, 0) 
                    self.dir.x = -1
            elif Key[pygame.K_s] == True:
                wall_above = False
                
                # After this runs, wall_above is True if there is a wall, and False if there is no wall
                for wall in self.groups_list['WALL']: #warning,list will break,switch to dict
                    walls_position = wall.rect.topleft
                    if  walls_position == (self.rect.topleft[0] + 0, self.rect.topleft[1] + 32 ): #If you try to walk through the block the input doesn't do anything
                        wall_above = True
                        wall_above = True
                # wall_above = True

                if wall_above == False: # If there is no wall above us, we move
                    self.rect.move_ip(0, +32)
                    self.dir.y = 1
            elif Key[pygame.K_d] == True:
                wall_above = False
                
                # After this runs, wall_above is True if there is a wall, and False if there is no wall
                for wall in self.groups_list['WALL']: #warning,list will break,switch to dict
                    walls_position = wall.rect.topleft
                    if  walls_position == (self.rect.topleft[0] + 32, self.rect.topleft[1] + 0):
                        wall_above = True
                # wall_above = True

                if wall_above == False: # If there is no wall above us, we move
                    self.rect.move_ip(+32, 0)
                    self.dir.x = 1
            self.timer = 0
        #pushing crates
        Crates = pygame.sprite.spritecollide(self, self.groups_list['CRATE'], False)
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

class Free(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Free.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Spike.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Lever(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("textures/Lever.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Ice(pygame.sprite.Sprite):
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