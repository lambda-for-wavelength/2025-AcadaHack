import pygame

TICK_RATE = 80

def distroy_game(groups):
    for i in groups.values():
        i.empty()

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
                self.player_terrain_interaction(0,-32)

                
            elif Key[pygame.K_a] == True:
                self.player_terrain_interaction(-32,0)
        
                
            elif Key[pygame.K_s] == True:
                self.player_terrain_interaction(0, 32)
                
               
            elif Key[pygame.K_d] == True:
                self.player_terrain_interaction(32,0)
                
           
            self.timer = 0
        #pushing crates
        Crates = pygame.sprite.spritecollide(self, self.groups_list['CRATE'], False)
        if len(Crates):
            for c in Crates:
                c.rect.move_ip(32 * self.dir.x, 32 * self.dir.y)

                other_crate = pygame.sprite.spritecollide(c, self.groups_list['CRATE'], False)
                if len(other_crate) != 1:
                    #move player and crate back

                    c.rect.move_ip(32 * - self.dir.x, 32 * - self.dir.y)
                    self.rect.move_ip(32 * - self.dir.x, 32 * - self.dir.y)  

                if pygame.sprite.spritecollide(c, self.groups_list['WALL'], False) or pygame.sprite.spritecollide(c, self.groups_list['SPIKE'], False):
                    #move player and crate back

                    c.rect.move_ip(32 * - self.dir.x, 32 * - self.dir.y)
                    self.rect.move_ip(32 * - self.dir.x, 32 * - self.dir.y)  
                    
                    
        Spikes = pygame.sprite.spritecollide(self, self.groups_list['SPIKE'], False)
        if len(Spikes):
            for s in Spikes:
                if s.frame:
                    distroy_game(self.groups_list)
                    self.kill()
    

    def player_terrain_interaction(self, x: int, y: int):
        
        # Check if about to move into a wall
        wall_above = False
        for wall in self.groups_list['WALL']: 
            walls_position = wall.rect.topleft
            if  walls_position == (self.rect.topleft[0] + x, self.rect.topleft[1] + y): #If you try to walk through the block the input doesn't do anything
                wall_above = True

        # Move if no wall right in front of us
        # if wall_above == False: # If there is no wall above us, we move
        #     self.rect.move_ip(x, y)
        #     self.dir.y = (y/32)
        #     self.dir.x = (x/32)

             # Check if about to move into a Ice
        ice_beside = False
        for ice in self.groups_list['ICE']: 
            ice_position = ice.rect.topleft
            if  ice_position == (self.rect.topleft[0] + x, self.rect.topleft[1] + y): #If you try to walk through the block the input doesn't do anything
                ice_beside = True

        crate_beside = False
        crate_beside2 = False
        if  ice_beside == True and wall_above == False:
            while ice_beside == True and wall_above == False: #on ice, with no wall
                self.rect.move_ip(x, y) # ONLY MOVES ON ICE
                self.dir.y = (y/32) 
                self.dir.x = (x/32)
                wall_above = False
                ice_beside =False
                # Scans every wall, and stops us from phasing
                for wall in self.groups_list['WALL']: 
                    walls_position = wall.rect.topleft
                    if  walls_position == (self.rect.topleft[0] + x, self.rect.topleft[1] + y): #If you try to walk through the block the input doesn't do anything
                        wall_above = True 
                # make us skate on ice
                for ice in self.groups_list['ICE']: 
                    ice_position = ice.rect.topleft   
                    if ice_position == (self.rect.topleft[0], self.rect.topleft[1]): #If you try to walk through the block the input doesn't do anything
                        ice_beside = True     
        elif wall_above == False: # If there is no wall above us, we move
            self.rect.move_ip(x, y)
            self.dir.y = (y/32)
            self.dir.x = (x/32)
        for crate in self.groups_list['CRATE']:
            crate_position = crate.rect.topleft
            if crate_position == (self.rect.topleft[0] + 0, self.rect.topleft[1] - y):
                crate_beside = True
            if crate_position == (self.rect.topleft[0] + 0, self.rect.topleft[1] - y*2):
                crate_beside2 = True
            if crate_beside ==True and crate_beside2 == True: 
                (self.rect.topleft[0] + x, self.rect.topleft[1] + y)
            
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
        self.image = pygame.Surface((32, 32))
        self.sheet = pygame.image.load("textures/Spike sheet.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.frame = 0
        self.time_f = [1000, 2000, 3000]
        self.timer = 0
    def update(self, dt):
        self.timer += dt
        for i in self.time_f:
            if self.timer <= i:
                self.image.blit(self.sheet, (0, 0), pygame.Rect(0, self.frame * 32, 32, 32))
            else:
                self.frame += 1
        if self.timer > self.time_f[-1]:
            self.timer = 0
            self.frame = 0

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

    