#blah blah blah

import pygame 
import objects
import Map_camera

pygame.init()

#Screen size in pixels 
Screen_Width = 320
Screen_Height = 320

#Makes a camera, Screen, and player
Screen = pygame.display.set_mode((Screen_Height, Screen_Height))
Camera_img = pygame.Surface((32*32, 32*32))
Camera_rect = Screen.get_rect()
clock = pygame.time.Clock()
player = objects.Player(Screen_Width/2, Screen_Height/2)
Map = pygame.image.load("textures/Map test.png")
Map_rect = Map.get_rect()
dt = 0
#Wall = pygame.rect((200, 120, 32, 32))
#camera = 

crate_g = pygame.sprite.Group()
c = objects.Crate(64, 64)
crate_g.add(c)

wall_g = pygame.sprite.Group()
w = objects.Wall(128, 128)
wall_g.add(w)

free_g = pygame.sprite.Group()
spike_g = pygame.sprite.Group()
lever_g = pygame.sprite.Group()
ice_g = pygame.sprite.Group()
wwt_g = pygame.sprite.Group()

groups = {'CRATE':crate_g, 'WALL':wall_g, 'FREE':free_g, 'SPIKE':spike_g, 'LEVER':lever_g, 'ICE':ice_g, 'WWT':wwt_g}
Map_camera.gen_map(pygame.image.load("textures/Map final.png"), groups)
player.groups_list = groups

#this is the game loop
run = True
while run == True:

    #this referches and draws the screen
    Camera_rect.center = (player.rect.center[0], player.rect.center[1])
    Screen.fill((0, 0, 0))
    Camera_img.fill((0, 0, 0))
    Camera_img.blit(player.image, player.rect)
    player.update(dt)
    crate_g.draw(Camera_img)
    crate_g.update(dt)
    wall_g.draw(Camera_img)
    wall_g.update(dt)
    #this is the camra stuff
    Screen.blit(Camera_img,(0, 0), Camera_rect)

    #this is the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    dt = clock.tick(60)

#This is to end the game
pygame.quit()