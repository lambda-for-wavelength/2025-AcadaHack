#blah blah blah

import pygame 
import objects
import Map_camera
import time

pygame.init()

#Screen size in pixels 
Screen_Width = 320
Screen_Height = 320
dt = 0
clock = pygame.time.Clock()

#Makes a camera, Screen, and player
Screen = pygame.display.set_mode((Screen_Height, Screen_Height))
Camera_img = pygame.Surface((32*32, 32*32))
Camera_rect = Screen.get_rect()
crate_g = pygame.sprite.Group()
wall_g = pygame.sprite.Group()
free_g = pygame.sprite.Group()
spike_g = pygame.sprite.Group()
lever_g = pygame.sprite.Group()
ice_g = pygame.sprite.Group()
wwt_g = pygame.sprite.Group()
player_g = pygame.sprite.Group()
groups = {'WALL':wall_g, 'FREE':free_g, 'SPIKE':spike_g, 'LEVER':lever_g, 'ICE':ice_g, 'WWT':wwt_g, 'CRATE':crate_g, 'PLAYER':player_g}

def setup_game():
    player = objects.Player(64, 32*30)
    player_g.add(player)
    #this crats the list groups
    Map_camera.gen_map(pygame.image.load("textures/Map test final.png"), groups)
    player.groups_list = groups
    return player


#this is the game loop
player = setup_game()
run = True
while run == True:

    #this referches and draws the screen
    Camera_rect.center = (player.rect.center[0], player.rect.center[1])
    Screen.fill((0, 0, 0))
    Camera_img.fill((0, 0, 0))
    for i in groups.values():
        i.draw(Camera_img)
        i.update(dt)
    #this is the camra stuff
    Screen.blit(Camera_img,(0, 0), Camera_rect)

    if len(player_g.sprites()) == 0:
        player = setup_game()

    #this is the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    dt = clock.tick(60)

#This is to end the game
pygame.quit()